# -*- coding: utf-8 -*-
import tornado.web
from dao.client import Client


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
