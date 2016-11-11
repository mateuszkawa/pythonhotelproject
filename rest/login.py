# -*- coding: utf-8 -*-
import tornado.httputil
import tornado.web
from dao.user import User
from dao.client import Client


class LoginREST(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self: tornado.web.RequestHandler):
        if not self.__handle_cookie():
            return
        print("it works!")
        import pprint
        pprint.pprint(self.request.arguments)
        for elem in self.request.arguments:
            print("%s: %s" % (elem, self.get_argument(elem)))
        self.redirect('/main')

    def __handle_cookie(self: tornado.web.RequestHandler):
        user = User.get_user(login=self.get_argument("inputLogin"), password=self.get_argument("inputPassword"))
        if user is None:
            self.redirect('/login')
            return False
        else:
            self.set_secure_cookie("user", Client.get_client(user.client).name, expires_days=0.4)
            self.set_secure_cookie("id", str(user.id), expires_days=0.4)
            self.set_secure_cookie("access_lvl", str(user.permission_level), expires_days=0.4)
            return True
