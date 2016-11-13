# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479075264.4568715
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
        __M_writer('<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>\r\n    <title>Main</title></head>\r\n<body> ')
        runtime._include_file(context, 'shared/menu.mako', _template_uri)
        __M_writer('\r\n<div class="container">\r\n    <form action="/rooms/filter" method="post">\r\n        <label for="date_start">Date Start:</label>\r\n        <input name="date_start" id="date_start" class="form-control" placeholder="2016/11/18" type="text">\r\n        <label for="date_end">Date End:</label>\r\n        <input name="date_end" id="date_end" class="form-control" placeholder="2016/11/21" type="text">\r\n        <button class="btn btn-lg btn-primary btn-block" type="submit">Filter</button>\r\n    </form>\r\n    <table class="table table-striped">\r\n        <thead>\r\n        <tr>\r\n            <th>Room Name</th>\r\n            <th>ID</th>\r\n        </tr>\r\n        </thead>\r\n        <tbody>\r\n')
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
{"filename": "templates/main_room_list.mako", "source_encoding": "ascii", "line_map": {"32": 30, "38": 32, "16": 0, "23": 1, "24": 7, "25": 7, "26": 24, "27": 25, "28": 26, "29": 26, "30": 27, "31": 27}, "uri": "main_room_list.mako"}
__M_END_METADATA
"""
