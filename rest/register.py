# -*- coding: utf-8 -*-
import tornado.httputil
import tornado.web
from dao.client import Client
from dao.user import User


class RegisterRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self: tornado.web.RequestHandler):
        client = Client(name=str(self.get_argument('FirstName')), surname=str(self.get_argument('LastName')))
        User.create_user(
            User(
                login=str(self.get_argument('Login')),
                password=str(self.get_argument('Password')),
                client=Client.create_client(client)))
        self.redirect('/login')
