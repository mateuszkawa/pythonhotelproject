# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup
from handler.helpers.menu import prepare_variables


class ReservationMakeHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self, room_id: str):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('reservation.mako')
        variables = dict()
        prepare_variables(self, variables=variables)
        self.prepare_variables_inner(variables, room_id)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def prepare_variables_inner(self, variables: dict, room_id: str):
        room_dict = dict()
        room_dict['id'] = room_id
        if self.get_cookie('collide') is not None:
            self.clear_cookie('collide')
            room_dict['collision'] = ''
        variables['room_dict'] = room_dict
