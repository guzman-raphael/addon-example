# from .plugin import discovered_plugins, verify_signature
from .plugin import override_all, override_list
plugin_name = 'message'

def msg():
    return 'hello there!'

# if 'message' in discovered_plugins:
#     # import
#     module_name = discovered_plugins['message']
#     module = __import__(module_name)
#     module_dict = module.__dict__

#     # update error stack
#     if '__certificate__' in module_dict and verify_signature(module_name):
#         print('passed!')
#         pass

#     # # override one specific method
#     # usr = getattr(module, 'usr')

#     # # override all methods - not a really good idea to do this...
#     try:
#         to_import = module.__all__
#     except AttributeError:
#         to_import = [name for name in module_dict if not name.startswith('_')]
#     globals().update({name: module_dict[name] for name in to_import})

override_list(plugin_name, globals(), ['msg'])