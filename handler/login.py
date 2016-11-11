# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup


class LoginHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('login.mako')
        response = template.render()
        self.write(response)


class LogoutHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        self.clear_all_cookies()
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('login.mako')
        response = template.render()
        self.write(response)
