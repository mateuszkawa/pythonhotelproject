# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup
from handler.helpers.menu import prepare_variables


class AdministratorsViewHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('administrators_view.mako')
        variables = dict()
        prepare_variables(self, variables=variables)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")


class AdministratorsAddClientViewHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('administrators_view_addclient.mako')
        variables = dict()
        prepare_variables(self, variables=variables)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")
