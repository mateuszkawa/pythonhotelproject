# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479149231.7647321
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
        __M_writer('<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\r\n    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>\r\n    <title>Main</title>\r\n</head>\r\n<body>\r\n')
        runtime._include_file(context, 'shared/menu.mako', _template_uri)
        __M_writer('\r\n<div class="container">\r\n    Hello\r\n</div>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "main_1.mako", "filename": "templates/main_1.mako", "source_encoding": "ascii", "line_map": {"16": 0, "29": 23, "21": 1, "22": 10, "23": 10}}
__M_END_METADATA
"""
