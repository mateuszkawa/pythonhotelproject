# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup


class MainPageHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('main_1.mako')
        response = template.render()
        self.write(response)

    def get_current_user(self):
        return self.get_secure_cookie("user")