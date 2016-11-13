# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479075406.223892
_enable_loop = True
_template_filename = 'templates/shared/menu.mako'
_template_uri = 'shared/menu.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        menu = context.get('menu', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<nav class="navbar navbar-default">\r\n  <div class="container-fluid">\r\n    <ul class="nav navbar-nav">\r\n      <li class="active"><a href="/main">Home</a></li>\r\n      <li><a href="/rooms">Rooms</a></li>\r\n')
        if menu['access_lvl'] < 3:
            __M_writer('      <li><a href="/admin">Admin</a></li>\r\n')
        __M_writer('    </ul>\r\n    <a class="navbar-brand navbar-right" href="/logout">LogOut</a>\r\n    <a class="navbar-brand navbar-right" href="/rooms/my">MyRooms</a>\r\n  </div>\r\n</nav>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "22": 1, "23": 6, "24": 7, "25": 9, "31": 25}, "source_encoding": "ascii", "filename": "templates/shared/menu.mako", "uri": "shared/menu.mako"}
__M_END_METADATA
"""
