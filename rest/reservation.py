# -*- coding: utf-8 -*-
import tornado.web
import mako.lookup
import datetime
from dao.room import Room
from dao.roomstate import RoomState
from handler.helpers.menu import prepare_variables


class ReservationPayHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self, room_state_id):
        room_state = RoomState.get_room_state_by_id(room_state_id)
        room_state.payment = True
        RoomState.update_room_state(room_state)
        self.redirect('/rooms/my')

    def get_current_user(self):
        return self.get_secure_cookie("user")


class ReservationCancelHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self, room_state_id):
        RoomState.delete_room_state(room_state_id)
        self.redirect('/rooms/my')


class ReservationCreateHandler(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def post(self, room_state_id):
        self.redirect('/rooms/my')
