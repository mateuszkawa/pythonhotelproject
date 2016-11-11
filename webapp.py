# -*- coding: utf-8 -*-
import base.webserver as webserver
from handler.register import RegistrationHandler
from rest.login import LoginREST
from handler.login import LoginHandler

webserver.url_mapper.extend((
    (r"/register", RegistrationHandler),
    (r"/login", LoginHandler),
    (r"/hotel/rest/login", LoginREST),
    ))

webserver.start(8090)
