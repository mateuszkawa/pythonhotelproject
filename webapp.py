# -*- coding: utf-8 -*-
import base.webserver as webserver
from handler.register import RegistrationHandler
from handler.login import LoginHandler, LogoutHandler
from handler.main import MainPageHandler
from handler.rooms import MainPageRoomHandler, MainPageRoomFilterHandler, MainPageRoomMyHandler
from handler.reservation import ReservationMakeHandler
from handler.client import MePageHandler
from handler.administrators import AdministratorsViewHandler, AdministratorsAddClientViewHandler, AdministratorsListClientsHandler
from handler.administrators import AdministratorsEditClientHandler, AdministratorsReservationHandler, AdministratorsShowReservationsHandler
from rest.reservation import ReservationCancelRest, ReservationPayRest, ReservationCreateRest
from rest.login import LoginRest
from rest.register import RegisterRest
from rest.client import MeUpdateRest
from rest.administrators import AdministratorsAddClientRest, AdministratorsEditClientRest, AdministratorsReservationCreateRest
from rest.administrators import AdministratorsShowReservationPayRest, AdministratorsShowReservationCancelRest

webserver.url_mapper.extend((
    (r"/register", RegistrationHandler),
    (r"/login", LoginHandler),
    (r"/main", MainPageHandler),
    (r"/hotel/rest/login", LoginRest),
    (r"/hotel/rest/register", RegisterRest),
    (r"/rooms", MainPageRoomHandler),
    (r"/rooms/filter", MainPageRoomFilterHandler),
    (r"/rooms/my", MainPageRoomMyHandler),
    (r"/reservation/pay/([^/]+)", ReservationPayRest),
    (r"/reservation/cancel/([^/]+)", ReservationCancelRest),
    (r"/reservation/make/([^/]+)", ReservationMakeHandler),
    (r"/reservation/create", ReservationCreateRest),
    (r"/me", MePageHandler),
    (r"/me/update", MeUpdateRest),
    (r"/administrators", AdministratorsViewHandler),
    (r"/administrators/addclientview", AdministratorsAddClientViewHandler),
    (r"/administrators/addclient", AdministratorsAddClientRest),
    (r"/administrators/listclients", AdministratorsListClientsHandler),
    (r"/administrators/edit/([^/]+)", AdministratorsEditClientHandler),
    (r"/administrators/editclient", AdministratorsEditClientRest),
    (r"/administrators/reservation", AdministratorsReservationHandler),
    (r"/administrators/reservation/make", AdministratorsReservationCreateRest),
    (r"/administrators/showreservations", AdministratorsShowReservationsHandler),
    (r"/administrators/showreservations/pay/([^/]+)", AdministratorsShowReservationPayRest),
    (r"/administrators/showreservations/cancel/([^/]+)", AdministratorsShowReservationCancelRest),
    (r"/logout", LogoutHandler)
    ))

webserver.start(8090)
