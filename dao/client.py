# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from dao import Base, get_engine
from sqlalchemy.orm import create_session


class Client(Base):
    __tablename__ = 'client'

    id = Column('client_id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    surname = Column('surname', String, nullable=False)

    @staticmethod
    def get_client(client_id: Integer) -> 'Client':
        session = create_session(bind=get_engine())
        client = session.query(Client).filter(Client.id == client_id).first()
        session.close()
        return client
