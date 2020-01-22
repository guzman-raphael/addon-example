from .plugin import override_all, override_list
plugin_name = 'message'

def msg():
    return 'hello there!'

override_list(plugin_name, globals(), ['msg'])