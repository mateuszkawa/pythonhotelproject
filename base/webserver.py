# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import os
from base.handler.filehandler import NoCacheStaticFileHandler

url_mapper = [
            (r"/(.*\.html)" , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.htm)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.txt)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.text)" , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.gif)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.bmp)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.png)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.jpg)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.js)"   , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.eot)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.otf)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.svg)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.ttf)"  , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.woff)" , tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.woff2)", tornado.web.StaticFileHandler, {'path': os.getcwd()}),
            (r"/(.*\.css)"  , NoCacheStaticFileHandler     , {'path': os.getcwd()})]


def start(port: int):
    application = tornado.web.Application(url_mapper)
    application.settings['cookie_secret'] = 'someRandomValueHotel'
    application.settings['login_url'] = '/login'
    application.listen(port)
    print('Service listen on {port}'.format(port=port))
    tornado.ioloop.IOLoop.instance().start()
