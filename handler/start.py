# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup


class HotelStartHandler(tornado.web.RequestHandler):
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('start.mako')
        variables = {'example_dictionary': {
                'example_key_1': 'example_value',
                'example_key_2': ['example_list_val_1', 'example_list_val_2', 'example_list_val_3']}}

        response = template.render(**variables)
        self.write(response)
