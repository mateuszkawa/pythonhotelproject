# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup


class TestHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('test.mako')
        response = template.render()
        self.write(response)
