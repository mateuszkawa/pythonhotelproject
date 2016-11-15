# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479231905.303921
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n            <div class="header header-filter" style="background-image: url(\'../assets/material/img/city.jpg\'); background-size: cover; background-position: top center;">\r\n                <div class="container">\r\n                    <div class="row">\r\n                        <div class="col-md-4 col-md-offset-4 col-sm-6 col-sm-offset-3">\r\n                            <div class="card card-signup">\r\n                                <form class="form-horizontal" role="form" method="post" action="/hotel/rest/register">\r\n                                    <div class="header header-primary text-center">\r\n                                        <h4>Sign Up</h4>\r\n                                    </div>\r\n                                    <div class="content">\r\n                                            <input id="Email" name="Email" type="text" class="form-control" placeholder="Email..."/>\r\n                                            <input id="Password" name="Password" type="password" placeholder="Password..." class="form-control" />\r\n                                            <input id="FirstName" name="FirstName" type="text" class="form-control" placeholder="First Name..."/>\r\n                                            <input id="LastName" name="LastName" type="text" class="form-control" placeholder="Last Name..."/>\r\n                                            <input id="Phone" name="Phone" type="text" class="form-control" placeholder="Phone..."/>\r\n                                    </div>\r\n                                    <div class="footer text-center">\r\n                                        <a href="#" class="btn btn-simple btn-primary btn-lg">Get Started</a>\r\n                                        <button type="submit" class="btn btn-default">Register</button>\r\n                                    </div>\r\n                                </form>\r\n                            </div>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "templates/register.mako", "uri": "register.mako", "source_encoding": "ascii", "line_map": {"32": 1, "27": 0, "38": 32}}
__M_END_METADATA
"""
