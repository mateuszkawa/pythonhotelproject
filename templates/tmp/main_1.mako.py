# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478901020.0620973
_enable_loop = True
_template_filename = 'templates/main_1.mako'
_template_uri = 'main_1.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\r\n    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>\r\n    <title>Main</title>\r\n</head>\r\n<body>\r\n<nav class="navbar navbar-default">\r\n  <div class="container-fluid">\r\n    <ul class="nav navbar-nav">\r\n      <li class="active"><a href="#">Home</a></li>\r\n      <li><a href="#">Rooms</a></li>\r\n    </ul>\r\n    <a class="navbar-brand navbar-right" href="/logout">LogOut</a>\r\n  </div>\r\n</nav>\r\n<div class="container">\r\n    CONTENT Hello\r\n</div>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "main_1.mako", "line_map": {"16": 0, "27": 21, "21": 1}, "filename": "templates/main_1.mako", "source_encoding": "ascii"}
__M_END_METADATA
"""
