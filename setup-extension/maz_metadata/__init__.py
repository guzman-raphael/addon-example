import os
import hashlib
from pathlib import Path
from distutils.errors import DistutilsSetupError

from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
# from setuptools import Command

__version__ = "0.2.2"

def assert_string(dist, attr, value):
    """Verify that value is a string list"""
    try:
        # verify that value is string
        assert isinstance(value, str)
    except (TypeError, ValueError, AttributeError, AssertionError):
        raise DistutilsSetupError(
            "%r must be a string (got %r)" % (attr, value)
        )

def write_arg(cmd, basename, filename, force=False):
    argname = os.path.splitext(basename)[0]
    arg_value = getattr(cmd.distribution, argname, None)
    # if arg_value is not None:
    #     arg_value = '\n'.join(arg_value) + '\n'
    # print('::raphael debug::')
    # print(cmd)
    # print(basename)
    # print(force)
    # print(argname)
    # print(filename)
    # print(arg_value)
    # print(hash_pkg(str(Path(filename).parents[0]).split('.')[0]))
    # print(sign(arg_value, hash_pkg(str(Path(filename).parents[0]).split('.')[0])))
    write_value = sign(arg_value, hash_pkg(str(Path(filename).parents[0]).split('.')[0]))
    # write_value = "raphael"
    cmd.write_or_delete_file(argname, filename, write_value, force)

def sign(privkey_path, data):
    with open(privkey_path, "rb") as key_file:
        private_key = load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend())
    signature = private_key.sign(
        data.encode(),
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256())
    return base64.b64encode(signature).decode('utf-8') + '\n'

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