# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String
from dao import Base, get_engine
from sqlalchemy.orm import create_session


class Room(Base):
    __tablename__ = 'room'

    id = Column('room_id', Integer, primary_key=True)
    name = Column('name', String, nullable=False)

    @staticmethod
    def get_room(room_id: Integer) -> 'Room':
        session = create_session(bind=get_engine())
        room = session.query(Room).filter(Room.id == room_id).first()
        session.close()
        return room

    @staticmethod
    def get_all_rooms() -> list('Room'):
        session = create_session(bind=get_engine())
        rooms = session.query(Room).all()
        session.close()
        return rooms
