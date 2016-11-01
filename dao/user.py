# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey
from dao import Base


class User(Base):
    '''
    permission_level:
        3 - standard client
        2 - recepcionist
        1 - accountant
        '''
    __tablename__ = 'user'

    id = Column('user_id', Integer, primary_key=True)
    login = Column('login', String, nullable=False)
    password = Column('password', String, nullable=False)
    permission_level = Column('permission_level', Integer, nullable=False, default=3)
    client = Column('client', Integer, ForeignKey('client.client_id'), nullable=True)
