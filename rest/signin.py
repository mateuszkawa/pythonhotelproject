# -*- coding: utf-8 -*-
import tornado.httputil
import tornado.web


class HotelSignInREST(tornado.web.RequestHandler):
    def post(self: tornado.web.RequestHandler):
        print("it works!")
        for elem in self.request.arguments:
            print("%s: %s" % (elem, self.request.get_argument(elem)))
        self.redirect('/hotel')
