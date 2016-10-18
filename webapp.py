# -*- coding: utf-8 -*-
import sys
import pythonhotelproject.base.webserver as webserver
from pythonhotelproject.handler.start import HotelStartHandler
from pythonhotelproject.rest.signin import HotelSignInREST

webserver.url_mapper.extend((
    (r"/hotel", HotelStartHandler),
    (r"/hotel/rest/signin", HotelSignInREST),
    ))

webserver.start(8090)