# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478284708.0490062
_enable_loop = True
_template_filename = 'templates/layout.mako'
_template_uri = 'layout.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        example_dictionary = context.get('example_dictionary', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!doctype html>\r\n<html lang="en">\r\n    <head>\r\n        <meta charset="utf-8" />\r\n        <meta http-equiv="X-UA-COMPATIBLE" content="IE=edge,chrome=1" />\r\n\r\n        <script type="text/javascript" src="/assets/material/js/jquery.min.js"></script>\r\n        <script type="text/javascript" src="/assets/material/js/bootstrap.min.js"></script>\r\n        <script type="text/javascript" src="/assets/material/js/bootstrap-datepicker.js"></script>\r\n        <script type="text/javascript" src="/assets/material/js/material.min.js"></script>\r\n        <link href="/assets/material/css/bootstrap.min.css" rel="stylesheet" />\r\n        <link href="/assets/material/css/material-kit.css" rel="stylesheet" />\r\n        <link href="/assets/custom/css/custom.css" rel="stylesheet" />\r\n        <title>Rejestracja konta</title>\r\n    </head>\r\n    <body class="signup-page">\r\n        <nav class="navbar navbar-absolute">\r\n            <div class="container">\r\n                <div class="navbar-header">\r\n                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n                         <span class="sr-only">Toggle navigation</span>\r\n                         <span class="icon-bar"></span>\r\n                         <span class="icon-bar"></span>\r\n                         <span class="icon-bar"></span>\r\n                    </button>\r\n                    <a class="navbar-brand" href="#">Hotel</a>\r\n                </div>\r\n\r\n                <!-- Collect the nav links, forms, and other content for toggling -->\r\n                     <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n                       <ul class="nav navbar-nav">\r\n\r\n')
        if example_dictionary['logged_in'] == 'true':
            __M_writer('                                <li><a href="#">Look for room</a></li>\r\n                                <li><a href="#">My reservations</a></li>\r\n')
        else:
            __M_writer('                                <li><a href="#">Register</a></li>\r\n                                <li><a href="#">Log in</a></li>\r\n')
        __M_writer('\r\n                       </ul>\r\n                     </div><!-- /.navbar-collapse -->\r\n            </div>\r\n        </nav>\r\n\r\n        <div class="wrapper">\r\n            ')
        __M_writer(str(self.body()))
        __M_writer('\r\n        </div>\r\n\r\n    </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "templates/layout.mako", "uri": "layout.mako", "line_map": {"16": 0, "36": 30, "23": 1, "24": 33, "25": 34, "26": 36, "27": 37, "28": 40, "29": 47, "30": 47}}
__M_END_METADATA
"""
