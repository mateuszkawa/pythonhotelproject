# -*- coding: utf-8 -*-
import base.webserver as webserver
from handler.register import RegistrationHandler
from handler.login import LoginHandler, LogoutHandler
from handler.main import MainPageHandler
from handler.rooms import MainPageRoomHandler, MainPageRoomFilterHandler, MainPageRoomMyHandler
from handler.reservation import ReservationMakeHandler
from rest.reservation import ReservationCancelRest, ReservationPayRest, ReservationCreateRest
from rest.login import LoginREST

webserver.url_mapper.extend((
    (r"/register", RegistrationHandler),
    (r"/login", LoginHandler),
    (r"/main", MainPageHandler),
    (r"/hotel/rest/login", LoginREST),
    (r"/rooms", MainPageRoomHandler),
    (r"/rooms/filter", MainPageRoomFilterHandler),
    (r"/rooms/my", MainPageRoomMyHandler),
    (r"/reservation/pay/([^/]+)", ReservationPayRest),
    (r"/reservation/cancel/([^/]+)", ReservationCancelRest),
    (r"/reservation/make/([^/]+)", ReservationMakeHandler),
    (r"/reservation/create", ReservationCreateRest),
    (r"/logout", LogoutHandler)
    ))

webserver.start(8090)
