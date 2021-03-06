import pkg_resources
import hashlib
from pathlib import Path
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
import re
import json
from json.decoder import JSONDecodeError
import os

DJ_PUB_KEY = '''
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDUMOo2U7YQ1uOrKU/IreM3AQP2
AXJC3au+S9W+dilxHcJ3e98bRVqrFeOofcGeRPoNc38fiLmLDUiBskJeVrpm29Wo
AkH6yhZWk1o8NvGMhK4DLsJYlsH6tZuOx9NITKzJuOOH6X1I5Ucs7NOSKnmu7g5g
WTT5kCgF5QAe5JN8WQIDAQAB
-----END PUBLIC KEY-----
'''

discovered_plugins = {	
    entry_point.module_name: entry_point.name
    for entry_point
    in pkg_resources.iter_entry_points('maz.plugins')
}
print(discovered_plugins)

def hash_pkg(pkgpath):
    ref = Path(pkgpath).absolute().parents[0]
    details = ''
    details = update_details_dir(pkgpath, ref, details)
    return hashlib.sha1('blob {}\0{}'.format(len(details), details).encode()).hexdigest()
 
def update_details_dir(dirpath, ref, details):
    paths = sorted(Path(dirpath).absolute().glob('*'))
    # walk a directory to collect info
    for path in paths:
        if 'pycache' not in str(path):
            if os.path.isdir(str(path)):
                details = update_details_dir(path, ref, details)
            else:
                details = update_details_file(path, ref, details)
    return details

def update_details_file(filepath, ref, details):
    if '.sig' not in str(filepath):
        with open(str(filepath), 'r') as f:
            data = f.read()
        # mode = oct(os.stat(str(filepath))[ST_MODE])[2:]
        mode = 100644
        hash = hashlib.sha1('blob {}\0{}'.format(len(data),data).encode()).hexdigest()
        stage_no = 0
        relative_path = str(filepath.relative_to(ref))
        details = '{}{} {} {}\t{}\n'.format(details, mode, hash, stage_no, relative_path)
    return details

def update_error_stack(module):
    
    try:
        pkg = pkg_resources.get_distribution(module.__name__)

        # # File approach
        # module_cert = Path(pkg.egg_info, '{}.sig'.format(module.__name__))
        # with open(module_cert, 'r') as f:
        #     signature = f.read()

        # License approach
        # metadata = dict(re.findall(r'([a-zA-Z0-9\-]+): (.*?)\n', pkg.get_metadata(pkg.PKG_INFO)))
        # signature = json.loads(metadata['License'])['certificate']

        # Custom meta approach
        # signature = pkg.get_metadata('{}.sig'.format(module.__name__))
        signature = pkg.get_metadata('maz.sig')

        pub_key = load_pem_public_key(bytes(DJ_PUB_KEY, 'UTF-8'), backend=default_backend())
        data = hash_pkg(module.__path__[0])
        pub_key.verify(base64.b64decode(signature.encode()), data.encode(), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        print('Cert verified.')
    except (FileNotFoundError, JSONDecodeError, InvalidSignature):
        print('Error stack updated.')


def override(addon_type, state, method_list=None):
    relevant_plugins = {k: v for k, v in discovered_plugins.items() if v == addon_type}
    if relevant_plugins:
        # import
        for module_name in relevant_plugins:
            module = __import__(module_name)
            module_dict = module.__dict__

            # update error stack
            update_error_stack(module)

            # override preference
            if method_list is not None:
                new_methods = [getattr(module, v) for v in method_list]
                state.update(dict(zip(method_list, new_methods)))
            else:
                try:
                    to_import = module.__all__
                except AttributeError:
                    to_import = [name for name in module_dict if not name.startswith('_')]
                state.update({name: module_dict[name] for name in to_import})

            # maybe?
            # state.update(dict(__version__=module.__version__))
