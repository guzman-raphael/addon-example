from .plugin import override_all, override_list
addon_key = 'plugins_message'

def msg():
    return 'hello there!'

override_list(addon_key, globals(), ['msg'])