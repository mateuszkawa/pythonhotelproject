# -*- coding: utf-8 -*-
import base.webserver as webserver
from handler.register import HotelRegisterHandler
from rest.signin import HotelSignInREST

webserver.url_mapper.extend((
    (r"/register", HotelRegisterHandler),
    (r"/hotel/rest/signin", HotelSignInREST),
    ))

webserver.start(8090)
