# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478112955.34487
_enable_loop = True
_template_filename = 'templates/test.mako'
_template_uri = 'test.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!doctype html>\r\n<html lang="en">\r\n    <head>\r\n        <meta charset="utf-8" />\r\n        <meta http-equiv="X-UA-COMPATIBLE" content="IE=edge,chrome=1" />\r\n\r\n        <link href="/assets/material/css/bootstrap.min.css" rel="stylesheet" />\r\n        <link href="/assets/material/css/material-kit.css" rel="stylesheet" />\r\n        <title>HOTEL</title>\r\n    </head>\r\n    <body>\r\n        Some test text\r\n\r\n    </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/test.mako", "line_map": {"16": 0, "27": 21, "21": 1}, "source_encoding": "ascii", "uri": "test.mako"}
__M_END_METADATA
"""
