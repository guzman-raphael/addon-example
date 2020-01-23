from .plugin import override_all, override_list
addon_type = 'user'

# default methods that can be overwritten
def usr():
    return 'root'

def show_usr():
    return 'result: {}'.format(usr())

# methods to override
# override_all(addon_type, globals())
override_list(addon_type, globals(), ['usr'])

#safe
def test():
    return 'example'