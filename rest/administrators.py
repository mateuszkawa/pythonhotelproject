# -*- coding: utf-8 -*-
import tornado.web
import datetime
from dao.client import Client
from dao.roomstate import RoomState


class AdministratorsAddClientRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def post(self):
        Client.create_client(Client(name=str(self.get_argument('name')),
                                    surname=str(self.get_argument('surname'))))
        self.redirect('/administrators')

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")


class AdministratorsEditClientRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def post(self):
        Client.update_client(Client(id=str(self.get_argument('client_id')),
                                    name=str(self.get_argument('name')),
                                    surname=str(self.get_argument('surname'))))
        self.redirect('/administrators/listclients')

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")


class AdministratorsReservationCreateRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")

    @tornado.web.authenticated
    def post(self):
        user_id = self.get_argument('user_id')
        room_id = self.get_argument('room_id')
        date_start = datetime.date(*tuple([int(x) for x in self.get_argument('date_start').split('/')]))
        date_end = datetime.date(*tuple([int(x) for x in self.get_argument('date_end').split('/')]))
        if date_start > date_end:
            self.set_cookie('collide', 'val')
            self.redirect('/administrators/reservation')
        elif RoomState.check_colliding_states_for_room(int(room_id), date_start, date_end) == []:
            room_state = RoomState(
                reserved_from=date_start,
                reserved_to=date_end,
                room=int(room_id),
                client=int(user_id))
            RoomState.persist_room_state(room_state)
            self.redirect('/administrators')
        else:
            self.set_cookie('collide', 'val')
            self.redirect('/administrators/reservation')


class AdministratorsShowReservationPayRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")

    @tornado.web.authenticated
    def get(self, room_state_id: str):
        room_state = RoomState.get_room_state_by_id(room_state_id)
        room_state.payment = True
        RoomState.update_room_state(room_state)
        self.redirect('/administrators/showreservations')


class AdministratorsShowReservationCancelRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get_current_user(self):
        if int(self.get_secure_cookie('access_lvl')) <= 2:
            return self.get_secure_cookie("user")

    @tornado.web.authenticated
    def get(self, room_state_id: str):
        RoomState.delete_room_state(room_state_id)
        self.redirect('/administrators/showreservations')
