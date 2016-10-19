# -*- coding: utf-8 -*-
import base.webserver as webserver
from handler.start import HotelStartHandler
from rest.signin import HotelSignInREST

webserver.url_mapper.extend((
    (r"/hotel", HotelStartHandler),
    (r"/hotel/rest/signin", HotelSignInREST),
    ))

webserver.start(8090)
