# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Date, ForeignKey
from dao import Base, get_engine
from sqlalchemy.orm import create_session
import datetime


class RoomState(Base):
    __tablename__ = 'roomstate'
    id = Column('state_id', Integer, primary_key=True)
    reserved_from = Column('reserved_from', Date, nullable=False)
    reserved_to = Column('reserved_to', Date, nullable=False)
    room = Column('room', Integer, ForeignKey('room.room_id'), nullable=False)

    @staticmethod
    def get_all_states_for_room(room_id: Integer) -> 'RoomState':
        session = create_session(bind=get_engine())
        room = session.query(RoomState).filter(RoomState.room == room_id).all()
        session.close()
        return room

    @staticmethod
    def get_all_states_for_room_after(room_id: Integer, date_after: datetime.date) -> 'RoomState':
        session = create_session(bind=get_engine())
        room = session.query(RoomState).filter(RoomState.room == room_id, RoomState.reserved_to < date_after).all()
        session.close()
        return room
