# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478940069.5856621
_enable_loop = True
_template_filename = 'templates/main_room_list.mako'
_template_uri = 'main_room_list.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        str = context.get('str', UNDEFINED)
        room_dict = context.get('room_dict', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\r\n    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>\r\n    <title>Main</title></head>\r\n<body> ')
        runtime._include_file(context, 'shared/menu.mako', _template_uri)
        __M_writer('\r\n<div class="container">\r\n    <table class="table table-striped">\r\n        <thead>\r\n        <tr>\r\n            <th>Room Name</th>\r\n            <th>ID</th>\r\n        </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        for room in room_dict:
            __M_writer('        <tr>\r\n            <td>')
            __M_writer(str(room_dict[room]['name']))
            __M_writer('</td>\r\n            <td>')
            __M_writer(str(str(room_dict[room]['id'])))
            __M_writer('</td>\r\n        </tr>\r\n')
        __M_writer('        </tbody>\r\n    </table>\r\n</div>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "main_room_list.mako", "line_map": {"32": 24, "38": 32, "16": 0, "23": 1, "24": 8, "25": 8, "26": 18, "27": 19, "28": 20, "29": 20, "30": 21, "31": 21}, "filename": "templates/main_room_list.mako"}
__M_END_METADATA
"""
