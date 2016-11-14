# -*- coding: utf-8 -*-
import tornado.web
import datetime
from dao.roomstate import RoomState


class ReservationPayRest(tornado.web.RequestHandler):
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


class ReservationCancelRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    @tornado.web.authenticated
    def get(self, room_state_id):
        RoomState.delete_room_state(room_state_id)
        self.redirect('/rooms/my')

    def get_current_user(self):
        return self.get_secure_cookie("user")


class ReservationCreateRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def get_current_user(self):
        return self.get_secure_cookie("user")

    @tornado.web.authenticated
    def post(self):
        room_id = self.get_argument('room_id')
        date_start = datetime.date(*tuple([int(x) for x in self.get_argument('date_start').split('/')]))
        date_end = datetime.date(*tuple([int(x) for x in self.get_argument('date_end').split('/')]))
        if RoomState.check_colliding_states_for_room(int(room_id), date_start, date_end) == []:
            room_state = RoomState(
                reserved_from=date_start,
                reserved_to=date_end,
                room=int(room_id),
                client=int(self.get_secure_cookie('id')))
            RoomState.persist_room_state(room_state)
            self.redirect('/rooms/my')
        else:
            self.redirect('/reservation/%s' % room_id, 350)
