# -*- coding: utf-8 -*-
import tornado.httputil
import tornado.web
from dao.client import Client


class MeUpdateREST(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self: tornado.web.RequestHandler):
        client = Client(id=int(self.get_secure_cookie('client_id')),
                        name=self.get_argument('name'),
                        surname=self.get_argument('surname'))
        Client.update_client(client)
        self.redirect('/me')
