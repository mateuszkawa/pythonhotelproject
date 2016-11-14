# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup
from dao.client import Client
from dao.user import User
from handler.helpers.menu import prepare_variables


class MePageHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('edit_self.mako')
        variables = dict()
        prepare_variables(self, variables=variables)
        self.prepare_additional_variables(variables)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        return self.get_secure_cookie('user')

    def prepare_additional_variables(self, variables):
        client_dict = dict()
        client = Client.get_client(int(self.get_secure_cookie('client_id')))
        client_dict['name'] = client.name
        client_dict['surname'] = client.surname
        variables['client_dict'] = client_dict
