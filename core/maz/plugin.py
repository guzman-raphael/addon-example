import pkg_resources
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64

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

def update_error_stack(module):
    pub_key = load_pem_public_key(bytes(DJ_PUB_KEY, 'UTF-8'), backend=default_backend())
    try:
        signature = base64.b64decode(module.__certificate__.encode())
        data = module.__githash__.encode()
        pub_key.verify(signature, data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    except (AttributeError, InvalidSignature):
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
