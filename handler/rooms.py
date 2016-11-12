# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup
from dao.room import Room


class MainPageRoomHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('main_room_list.mako')
        variables = {'room_dict': self.prepare_rooms()}
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def prepare_rooms(self) -> dict:
        result_dict = dict()
        for room in Room.get_all_rooms():
            result_dict[room.id] = {
                'name'  : room.name,
                'id'    : room.id}
        return result_dict
