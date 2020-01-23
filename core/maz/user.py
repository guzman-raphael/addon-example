from .plugin import override
addon_type = 'user'

# default methods that can be overwritten
def usr():
    return 'root'

def show_usr():
    return 'result: {}'.format(usr())

# methods to override
# override(addon_type, globals())
override(addon_type, globals(), ['usr'])

#safe
def test():
    return 'example'