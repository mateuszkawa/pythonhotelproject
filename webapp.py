# -*- coding: utf-8 -*-
import base.webserver as webserver
from handler.register import RegistrationHandler
from handler.login import LoginHandler, LogoutHandler
from handler.main import MainPageHandler
from rest.login import LoginREST

webserver.url_mapper.extend((
    (r"/register", RegistrationHandler),
    (r"/login", LoginHandler),
    (r"/main", MainPageHandler),
    (r"/hotel/rest/login", LoginREST),
    (r"/logout", LogoutHandler)
    ))

webserver.start(8090)
