from tornado.web import RequestHandler


def get_menu_data(request: RequestHandler) -> dict:
    result_dict = dict()
    result_dict['name'] = request.get_secure_cookie('user')
    result_dict['access_lvl'] = request.get_secure_cookie('access_lvl')
    result_dict['id'] = request.get_secure_cookie('id')
    return result_dict


def prepare_variables(request: RequestHandler, variables: dict):
    menu_dict = dict()
    menu_dict['name'] = request.get_secure_cookie('user')
    menu_dict['access_lvl'] = int(request.get_secure_cookie('access_lvl'))
    menu_dict['id'] = int(request.get_secure_cookie('id'))
    variables['menu'] = menu_dict
