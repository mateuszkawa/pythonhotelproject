# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup
from handler.helpers.menu import prepare_variables
from dao.client import Client
from dao.room import Room
from dao.roomstate import RoomState


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


class AdministratorsListClientsHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('administrators_view_listclients.mako')
        variables = dict()
        prepare_variables(self, variables=variables)
        self.additional_variables_prepare(variables)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")

    def additional_variables_prepare(self, variables: dict):
        clients = Client.get_all_clients()
        client_dict = dict()
        for client in clients:
            client_dict[client.id] = dict()
            client_dict[client.id]['id'] = client.id
            client_dict[client.id]['name'] = client.name
            client_dict[client.id]['surname'] = client.surname
        variables['client_dict'] = client_dict


class AdministratorsEditClientHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self, client_id: str):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('administrators_view_editclient.mako')
        variables = dict()
        prepare_variables(self, variables=variables)
        self.additional_variables_prepare(variables, client_id)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")

    def additional_variables_prepare(self, variables: dict, client_id: str):
        client = Client.get_client(int(client_id))
        client_dict = dict()
        client_dict['id'] = client.id
        client_dict['name'] = client.name
        client_dict['surname'] = client.surname
        variables['client_dict'] = client_dict


class AdministratorsReservationHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('administrators_view_reservation.mako')
        variables = dict()
        prepare_variables(self, variables=variables)
        self.additional_variables_prepare(variables)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")

    def additional_variables_prepare(self, variables: dict):
        if self.get_cookie('collide') is not None:
            self.clear_cookie('collide')
            variables['collision'] = ''

        clients = Client.get_all_clients()
        client_dict = dict()
        for client in clients:
            client_dict[client.id] = dict()
            client_dict[client.id]['id'] = client.id
            client_dict[client.id]['name'] = client.name
            client_dict[client.id]['surname'] = client.surname
        variables['client_dict'] = client_dict

        rooms_dict = dict()
        rooms = Room.get_all_rooms()
        for room in rooms:
            rooms_dict[room.id] = dict()
            rooms_dict[room.id]['id'] = room.id
            rooms_dict[room.id]['name'] = room.name
        variables['rooms_dict'] = rooms_dict

class AdministratorsShowReservationsHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('administrators_view_showreservations.mako')
        variables = dict()
        prepare_variables(self, variables=variables)
        self.additional_variables_prepare(variables)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")

    def additional_variables_prepare(self, variables: dict):
        clients = Client.get_all_clients()
        client_dict = dict()
        for client in clients:
            client_dict[client.id] = dict()
            client_dict[client.id]['id'] = client.id
            client_dict[client.id]['name'] = client.name
            client_dict[client.id]['surname'] = client.surname
            room_states_dict = dict()
            roomstates = RoomState.get_all_room_states_for_client(client_id=client.id)
            for room_state in roomstates:
                room_states_dict[room_state.id] = dict()
                room_states_dict[room_state.id]['room_name'] = Room.get_room(room_state.room).name
                room_states_dict[room_state.id]['reserved_from'] = room_state.reserved_from
                room_states_dict[room_state.id]['reserved_to'] = room_state.reserved_to
                if room_state.payment:
                    room_states_dict[room_state.id]['state'] = 'PAYED'
                else:
                    room_states_dict[room_state.id]['state'] = 'RESERVED'
                room_states_dict[room_state.id]['pay'] = room_state.payment
            client_dict[client.id]['roomstates'] = room_states_dict
        variables['client_dict'] = client_dict
