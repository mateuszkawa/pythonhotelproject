# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import os

class BigFileHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self, file_path: str):
        buf_size = 65536
        self.set_header('Content-Length', os.path.getsize(file_path))
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=' + file_path)
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(buf_size)
                if not data:
                    break
                    self.write(data)
                    yield self.flush()
        self.finish()


class NoCacheStaticFileHandler(tornado.web.StaticFileHandler):
    def set_extra_headers(self, path):
        self.set_header('Cache-control', 'no-cache')
