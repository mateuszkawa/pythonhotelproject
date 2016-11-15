# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479241444.7900512
_enable_loop = True
_template_filename = 'templates/register.mako'
_template_uri = 'register.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>\r\n    <title>Login</title>\r\n</head>\r\n<body>\r\n<div class="container">\r\n    <div class="row">\r\n        <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3">\r\n            <div class="card card-signup">\r\n                <form class="form-signin" action="/hotel/rest/register" method="post">\r\n                    <input id="Login" name="Login" type="text" class="form-control" placeholder="Login..." />\r\n                    <input id="Password" name="Password" type="password" placeholder="Password..." class="form-control"/>\r\n                    <input id="FirstName" name="FirstName" type="text" class="form-control" placeholder="First Name..."/>\r\n                    <input id="LastName" name="LastName" type="text" class="form-control" placeholder="Last Name..."/>\r\n                    <button class="btn btn-lg btn-primary btn-block" type="submit">Register</button>\r\n                </form>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 0, "27": 21, "21": 1}, "filename": "templates/register.mako", "uri": "register.mako"}
__M_END_METADATA
"""
