from .plugin import override_all, override_list
plugin_name = 'user'

# default methods that can be overwritten
def usr():
    return 'root'

def show_usr():
    return 'result: {}'.format(usr())

# methods to override
override_all(plugin_name, globals())
# override_list(plugin_name, globals(), ['usr'])

#safe
def test():
    return 'example'