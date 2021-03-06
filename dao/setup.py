# -*- coding: utf-8 -*-
import datetime
from dao import Base, get_engine
from sqlalchemy.orm import create_session
from dao.client import Client
from dao.user import User
from dao.room import Room
from dao.roomstate import RoomState

session = create_session(bind=get_engine())


def create_tables(engine):
    Base.metadata.create_all(engine)


def create_sample_data():
    if get_engine().dialect.has_table(get_engine(), 'user'):
        return
    conn = get_engine()
    create_tables(conn)

    #add some client
    session.begin()
    for client in [Client(name=('example_name_%s' % x), surname=('example_surname_%s' % x)) for x in range(1, 4)]:
        session.add(client)
    session.commit()

    #add some user
    session.begin()
    for user in [User(login=('user_%s' % x), password=('user_%s' % x), client=x, permission_level=x) for x in range(1, 4)]:
        session.add(user)
    session.commit()

    #add some rooms
    session.begin()
    for room in [Room(name=('room_%s' % x)) for x in range(1, 4)]:
        session.add(room)
    session.commit()

    #add some reservations
    session.begin()
    for roomstate in [RoomState(
            reserved_from=datetime.date(2016, 11, 15),
            reserved_to=datetime.date(2016, 11, 17 + x),
            room=x,
            client=3) for x in range(1, 4)]:
        session.add(roomstate)
    session.commit()

if __name__ == '__main__':
    create_sample_data()
    users = session.query(User)
    for user in users:
        print(user.login)
    print("done")
