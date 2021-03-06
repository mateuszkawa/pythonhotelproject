# -*- coding: utf-8 -*-
import tornado.httputil
import tornado.web
from dao.user import User
from dao.client import Client


class LoginRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self: tornado.web.RequestHandler):
        if not self.__handle_cookie():
            return
        self.redirect('/main')

    def __handle_cookie(self: tornado.web.RequestHandler):
        user = User.get_user(login=self.get_argument('inputLogin'), password=self.get_argument('inputPassword'))
        if user is None:
            self.redirect('/login')
            return False
        else:
            self.set_secure_cookie('user', Client.get_client(user.client).name, expires_days=0.4)
            self.set_secure_cookie('id', str(user.id), expires_days=0.4)
            self.set_secure_cookie('client_id', str(user.client), expires_days=0.4)
            self.set_secure_cookie('access_lvl', str(user.permission_level), expires_days=0.4)
            return True
