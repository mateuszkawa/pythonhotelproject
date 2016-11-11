# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478890193.9692936
_enable_loop = True
_template_filename = 'templates/login.mako'
_template_uri = 'login.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\r\n    <link href="/assets/bootstrap/css/bootstrap.min.css" rel="stylesheet"/>\r\n    <title>Login</title>\r\n</head>\r\n<body>\r\n<div class="container">\r\n    <div class="row">\r\n        <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3">\r\n            <div class="card card-signup">\r\n                <form class="form-signin" action="/hotel/rest/login" method="post">\r\n                    <h2 class="form-signin-heading">Please Login</h2>\r\n                    <label for="inputLogin" class="sr-only">Login</label>\r\n                    <input name="inputLogin" id="inputLogin" class="form-control" placeholder="Login" required="" autofocus=""\r\n                           type="text">\r\n                    <label for="inputPassword" class="sr-only">Password</label>\r\n                    <input name="inputPassword" id="inputPassword" class="form-control" placeholder="Password" required="" type="password">\r\n                    <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>\r\n                </form>\r\n            </div>\r\n        </div>\r\n    </div>\r\n</div>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "templates/login.mako", "uri": "login.mako", "line_map": {"16": 0, "27": 21, "21": 1}}
__M_END_METADATA
"""
