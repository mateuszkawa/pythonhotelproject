# -*- coding: utf-8 -*-
from dao import Base, get_engine
from sqlalchemy.orm import create_session
from dao.client import Client
from dao.user import User

session = create_session(bind=get_engine())


def create_tables(engine):
    Base.metadata.create_all(engine)


def create_sample_data():
    if get_engine().dialect.has_table(get_engine(), 'user'):
        return
    conn = get_engine()
    create_tables(conn)

    session.begin()
    client = Client(name='example_name_1', surname='example_surname_1')
    session.add(client)
    session.commit()

    session.begin()
    user = User(login='user_1', password='user_1', client=client.id)
    session.add(user)
    session.commit()

if __name__ == '__main__':
    create_sample_data()
    users = session.query(User)
    for user in users:
        print(user.login)
    print("done")
