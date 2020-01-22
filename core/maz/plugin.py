import pkg_resources
discovered_plugins = {
    entry_point.name: entry_point.module_name
    for entry_point
    in pkg_resources.iter_entry_points('maz.plugins')
}

print(discovered_plugins)

def verify_signature(module_name):
    return True

def override_all(plugin_name, state):
    if plugin_name in discovered_plugins:
        # import
        module_name = discovered_plugins[plugin_name]
        module = __import__(module_name)
        module_dict = module.__dict__

        # update error stack
        if '__certificate__' in module_dict and verify_signature(module_name):
            print('passed!')
            pass

        # # override all methods - not usually a good idea to do this...
        try:
            to_import = module.__all__
        except AttributeError:
            to_import = [name for name in module_dict if not name.startswith('_')]
        state.update({name: module_dict[name] for name in to_import})
        # maybe?
        state.update(dict(__version__=module.__version__))

def override_list(plugin_name, state, method_list):
    if plugin_name in discovered_plugins:
        # import
        module_name = discovered_plugins[plugin_name]
        module = __import__(module_name)
        module_dict = module.__dict__

        # update error stack
        if '__certificate__' in module_dict and verify_signature(module_name):
            print('passed!')
            pass

        # override specific methods
        new_methods = [getattr(module, v) for v in method_list]
        state.update(dict(zip(method_list, new_methods)))
        # maybe?
        state.update(dict(__version__=module.__version__))



