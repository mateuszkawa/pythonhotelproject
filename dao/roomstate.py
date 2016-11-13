# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Date, ForeignKey, or_, and_
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
        states = session.query(RoomState).filter(RoomState.room == room_id).all()
        session.close()
        return states

    @staticmethod
    def get_all_states_for_room_after(room_id: Integer, date_after: datetime.date) -> 'RoomState':
        session = create_session(bind=get_engine())
        states = session.query(RoomState).filter(RoomState.room == room_id, RoomState.reserved_to < date_after).all()
        session.close()
        return states

    @staticmethod
    def check_colliding_states_for_room(room_id: Integer, date_start: datetime.date, date_end: datetime.date):
        session = create_session(bind=get_engine())
        states = session.query(RoomState).filter(
            RoomState.room == room_id
        ).filter(
            or_(
                and_(RoomState.reserved_from > date_start, RoomState.reserved_from < date_end),
                and_(RoomState.reserved_to > date_start, RoomState.reserved_to < date_end),
                and_(RoomState.reserved_from > date_start, RoomState.reserved_to < date_end),
                and_(RoomState.reserved_from < date_start, RoomState.reserved_to > date_end))).all()
        session.close()
        return states


if __name__ == '__main__':
    print(RoomState.check_colliding_states_for_room(1, datetime.date(2016, 11, 18), datetime.date(2016, 11, 21)) == [])
    for state in RoomState.check_colliding_states_for_room(1, datetime.date(2016, 11, 18), datetime.date(2016, 11, 21)):
        print("from: %s, to: %s" % (state.reserved_from, state.reserved_to))
