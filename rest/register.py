# -*- coding: utf-8 -*-
import tornado.httputil
import tornado.web


class RegisterRest(tornado.web.RequestHandler):
    def data_received(self, chunk):
        pass

    def post(self: tornado.web.RequestHandler):
        #TODO: Implement Register functionality
        self.redirect('/main')
