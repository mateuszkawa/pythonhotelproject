# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup
import datetime
from dao.room import Room
from dao.roomstate import RoomState
from handler.helpers.menu import prepare_variables


class MainPageRoomHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('main_room_list.mako')
        variables = {'room_dict': self.prepare_rooms()}
        prepare_variables(self, variables=variables)
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


class MainPageRoomFilterHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def post(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('main_room_list.mako')
        variables = {'room_dict': self.prepare_rooms()}
        prepare_variables(self, variables=variables)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def prepare_rooms(self) -> dict:
        result_dict = dict()
        date_start = datetime.date(*tuple([int(x) for x in self.get_argument('date_start').split('/')]))
        date_end = datetime.date(*tuple([int(x) for x in self.get_argument('date_end').split('/')]))
        for room in Room.get_all_rooms():
            if RoomState.check_colliding_states_for_room(room.id, date_start=date_start, date_end=date_end) == []:
                result_dict[room.id] = {
                    'name'  : room.name,
                    'id'    : room.id}
        return result_dict


class MainPageRoomMyHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('main_room_list_my.mako')
        variables = {'room_dict': self.prepare_room_states()}
        prepare_variables(self, variables=variables)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def prepare_room_states(self) -> dict:
        result_dict = dict()
        room_states = RoomState.get_all_room_states_for_client(int(self.get_secure_cookie('id')))
        for room_state in room_states:
            if room_state.room not in result_dict:
                result_dict[room_state.room] = dict()
            result_dict[room_state.room][room_state.id] = dict()
            result_dict[room_state.room][room_state.id]['name'] = Room.get_room(room_state.room).name
            result_dict[room_state.room][room_state.id]['date_from'] = room_state.reserved_from
            result_dict[room_state.room][room_state.id]['date_to'] = room_state.reserved_to
            if room_state.payment:
                result_dict[room_state.room][room_state.id]['state'] = 'PAYED'
            else:
                result_dict[room_state.room][room_state.id]['state'] = 'RESERVED'
            result_dict[room_state.room][room_state.id]['pay'] = room_state.payment
            result_dict[room_state.room][room_state.id]['id'] = room_state.id
        return result_dict

