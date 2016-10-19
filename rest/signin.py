# -*- coding: utf-8 -*-
import tornado.httputil
import tornado.web


class HotelSignInREST(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self: tornado.web.RequestHandler):
        print("it works!")
        for elem in self.request.arguments:
            print("%s: %s" % (elem, self.get_argument(elem)))
        self.redirect('/hotel')
