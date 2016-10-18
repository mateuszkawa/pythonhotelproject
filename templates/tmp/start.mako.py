# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1476810049.8706048
_enable_loop = True
_template_filename = 'templates/start.mako'
_template_uri = 'start.mako'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        example_dictionary = context.get('example_dictionary', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<!doctype html>\r\n<html lang="en">\r\n    <head>\r\n        <meta charset="utf-8" />\r\n        <meta http-equiv="X-UA-COMPATIBLE" content="IE=edge,chrome=1" />\r\n\r\n        <link href="/assets/material/css/bootstrap.min.css" rel="stylesheet" />\r\n        <link href="/assets/material/css/material-kit.css" rel="stylesheet" />\r\n        <title>HOTEL</title>\r\n    </head>\r\n    <body class="signup-page">\r\n        <nav class="navbar navbar-transparent navbar-absolute">\r\n            <div class="container">\r\n                <div class="navbar-header">\r\n                    Menu?\r\n                </div>\r\n            </div>\r\n        </nav>\r\n\r\n        <div class="wrapper">\r\n            <div class="header header-filter" style="background-image: url(\'../assets/material/img/city.jpg\'); background-size: cover; background-position: top center;">\r\n                <div class="container">\r\n                    <div class="row">\r\n                        <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3">\r\n                            <div class="card card-signup">\r\n                                <form class="form-horizontal" role="form" method="post" action="/hotel/rest/signin">\r\n                                    <div class="header header-primary text-center">\r\n                                        <h4>Sign Up</h4>\r\n                                    </div>\r\n                                    <p class="text-divider">Or Be Classical</p>\r\n                                    <div class="content">\r\n\r\n                                        <div class="input-group">\r\n                                            <span class="input-group-addon">\r\n                                                <i class="material-icons">login</i>\r\n                                            </span>\r\n                                            <input type="text" class="form-control" placeholder="First Name...">\r\n                                        </div>\r\n\r\n                                        <div class="input-group">\r\n                                            <span class="input-group-addon">\r\n                                                <i class="material-icons">email</i>\r\n                                            </span>\r\n                                            <input type="text" class="form-control" placeholder="Email...">\r\n                                        </div>\r\n\r\n                                        <div class="input-group">\r\n                                            <span class="input-group-addon">\r\n                                                <i class="material-icons">password</i>\r\n                                            </span>\r\n                                            <input type="password" placeholder="Password..." class="form-control" />\r\n                                        </div>\r\n                                    </div>\r\n                                    <div class="input-group">\r\n                                        <span class="input-group-addon">\r\n                                            <i class="material-icons">Mako example usage:</i>\r\n                                            ')
        __M_writer(str(example_dictionary['example_key_1']))
        __M_writer('\r\n')
        for elem in example_dictionary['example_key_2']:
            if elem == 'example_list_val_2':
                __M_writer('                                                    <div><span><h4>')
                __M_writer(str(elem))
                __M_writer('</h4></span></div>\r\n')
            else:
                __M_writer('                                                    <div><span><i>')
                __M_writer(str(elem))
                __M_writer('</i></span></div>\r\n')
        __M_writer('                                        </span>\r\n                                    </div>\r\n                                    <div class="footer text-center">\r\n                                        <a href="#" class="btn btn-simple btn-primary btn-lg">Get Started</a>\r\n                                        <button type="submit" class="btn btn-default">Sign In</button>\r\n                                    </div>\r\n                                </form>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n\r\n    </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "start.mako", "source_encoding": "ascii", "line_map": {"32": 63, "33": 63, "34": 66, "40": 34, "16": 0, "22": 1, "23": 58, "24": 58, "25": 59, "26": 60, "27": 61, "28": 61, "29": 61, "30": 62, "31": 63}, "filename": "templates/start.mako"}
__M_END_METADATA
"""
