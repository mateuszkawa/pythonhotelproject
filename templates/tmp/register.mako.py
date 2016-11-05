# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478284708.0350056
_enable_loop = True
_template_filename = 'templates/register.mako'
_template_uri = 'register.mako'
_source_encoding = 'ascii'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'layout.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        example_dictionary = context.get('example_dictionary', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n            <div class="header header-filter" style="background-image: url(\'../assets/material/img/city.jpg\'); background-size: cover; background-position: top center;">\r\n                <div class="container">\r\n                    <div class="row">\r\n                        <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3">\r\n                            <div class="card card-signup">\r\n                                <form class="form-horizontal" role="form" method="post" action="/hotel/rest/signin">\r\n                                    <div class="header header-primary text-center">\r\n                                        <h4>Sign Up</h4>\r\n                                    </div>\r\n                                    <p class="text-divider">Or Be Classical</p>\r\n                                    <div class="content">\r\n\r\n                                        <div class="input-group">\r\n                                            <span class="input-group-addon">\r\n                                                <i class="material-icons">login</i>\r\n                                            </span>\r\n                                            <input type="text" class="form-control" placeholder="First Name...">\r\n                                        </div>\r\n\r\n                                        <div class="input-group">\r\n                                            <span class="input-group-addon">\r\n                                                <i class="material-icons">email</i>\r\n                                            </span>\r\n                                            <input type="text" class="form-control" placeholder="Email...">\r\n                                        </div>\r\n\r\n                                        <div class="input-group">\r\n                                            <span class="input-group-addon">\r\n                                                <i class="material-icons">password</i>\r\n                                            </span>\r\n                                            <input type="password" placeholder="Password..." class="form-control" />\r\n                                        </div>\r\n                                    </div>\r\n                                    <div class="input-group">\r\n                                        <span class="input-group-addon">\r\n                                            <i class="material-icons">Mako example usage:</i>\r\n                                            ')
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
        __M_writer('                                        </span>\r\n                                    </div>\r\n                                    <div class="footer text-center">\r\n                                        <a href="#" class="btn btn-simple btn-primary btn-lg">Get Started</a>\r\n                                        <button type="submit" class="btn btn-default">Sign In</button>\r\n                                    </div>\r\n                                </form>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "templates/register.mako", "uri": "register.mako", "line_map": {"33": 1, "34": 40, "35": 40, "36": 41, "37": 42, "38": 43, "39": 43, "40": 43, "41": 44, "42": 45, "43": 45, "44": 45, "45": 48, "51": 45, "27": 0}}
__M_END_METADATA
"""
