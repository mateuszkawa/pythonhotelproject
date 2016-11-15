# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup
from handler.helpers.menu import prepare_variables
from dao.client import Client
from dao.room import Room
from dao.roomstate import RoomState


class AccountantHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self):
        template_lookup = mako.lookup.TemplateLookup(directories=['templates'], module_directory='templates/tmp')
        template = template_lookup.get_template('accountant_view.mako')
        variables = dict()
        prepare_variables(self, variables=variables)
        self.additional_variables_prepare(variables)
        response = template.render(**variables)
        self.write(response)

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) < 2:
            return self.get_secure_cookie("user")

    def additional_variables_prepare(self, variables: dict):
        clients = Client.get_all_clients()
        client_dict = dict()
        state_dict_payed = dict()
        state_dict_unpayed = dict()
        for client in clients:
            client_dict[client.id] = dict()
            client_dict[client.id]['client_name'] = client.name
            client_dict[client.id]['client_surname'] = client.surname
            states = RoomState.get_all_room_states_for_client(client.id)
            for state in states:
                if state.payment:
                    state_dict_payed[state.id] = dict()
                    state_dict_payed[state.id]['client_id'] = client.id
                    state_dict_payed[state.id]['room_name'] = Room.get_room(state.room).name
                    state_dict_payed[state.id]['reserved_from'] = state.reserved_from
                    state_dict_payed[state.id]['reserved_to'] = state.reserved_to
                    if state.payment:
                        state_dict_payed[state.id]['state'] = 'PAYED'
                    else:
                        state_dict_payed[state.id]['state'] = 'RESERVED'
                else:
                    state_dict_unpayed[state.id] = dict()
                    state_dict_unpayed[state.id]['client_id'] = client.id
                    state_dict_unpayed[state.id]['room_name'] = Room.get_room(state.room).name
                    state_dict_unpayed[state.id]['reserved_from'] = state.reserved_from
                    state_dict_unpayed[state.id]['reserved_to'] = state.reserved_to
                    if state.payment:
                        state_dict_unpayed[state.id]['state'] = 'PAYED'
                    else:
                        state_dict_unpayed[state.id]['state'] = 'RESERVED'
        variables['client_dict'] = client_dict
        variables['state_dict_payed_dict'] = state_dict_payed
        variables['state_dict_unpayed_dict'] = state_dict_unpayed