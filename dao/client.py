# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from dao import Base


class Client(Base):
    __tablename__ = 'client'

    id = Column('client_id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)
    surname = Column('surname', String, nullable=False)
