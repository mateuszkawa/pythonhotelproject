# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, Boolean, Date, ForeignKey, or_, and_
from dao import Base, get_engine
from sqlalchemy.orm import create_session
import datetime


class RoomState(Base):
    __tablename__ = 'roomstate'
    id = Column('state_id', Integer, primary_key=True)
    reserved_from = Column('reserved_from', Date, nullable=False)
    reserved_to = Column('reserved_to', Date, nullable=False)
    room = Column('room', Integer, ForeignKey('room.room_id'), nullable=False)
    client = Column('client', Integer, ForeignKey('client.client_id'), nullable=False)
    payment = Column('payment', Boolean, default=False)

    @staticmethod
    def get_all_states_for_room(room_id: Integer) -> list('RoomState'):
        session = create_session(bind=get_engine())
        states = session.query(RoomState).filter(RoomState.room == room_id).all()
        session.close()
        return states

    @staticmethod
    def get_all_states_for_room_after(room_id: Integer, date_after: datetime.date) -> list('RoomState'):
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

    @staticmethod
    def get_all_room_states_for_client(client_id: Integer) -> list('RoomState'):
        session = create_session(bind=get_engine())
        result_room_states = session.query(RoomState).filter(RoomState.client == client_id).all()
        session.close()
        return result_room_states

    @staticmethod
    def get_room_state_by_id(room_state_id: int) -> 'RoomState':
        session = create_session(bind=get_engine())
        result_room_state = session.query(RoomState).filter(RoomState.id == room_state_id).first()
        session.close()
        return result_room_state

    @staticmethod
    def update_room_state(room_state: 'RoomState'):
        session = create_session(bind=get_engine())
        session.begin()
        room_state_in_database = session.query(RoomState).filter(RoomState.id == room_state.id).first()
        room_state_in_database.reserved_from = room_state.reserved_from
        room_state_in_database.reserved_to =room_state.reserved_to
        room_state_in_database.room = room_state.room
        room_state_in_database.client = room_state.client
        room_state_in_database.payment = room_state.payment
        session.commit()
        session.close()

    @staticmethod
    def delete_room_state(room_state_id: int):
        session = create_session(bind=get_engine())
        session.begin()
        session.query(RoomState).filter(RoomState.id == room_state_id).delete(synchronize_session=False)
        session.commit()
        session.close()

    @staticmethod
    def persist_room_state(room_state: 'RoomState'):
        session = create_session(bind=get_engine())
        session.begin()
        session.add(room_state)
        session.commit()
        session.close()

if __name__ == '__main__':
    print(RoomState.check_colliding_states_for_room(1, datetime.date(2016, 11, 18), datetime.date(2016, 11, 21)) == [])
    for state in RoomState.check_colliding_states_for_room(1, datetime.date(2016, 11, 18), datetime.date(2016, 11, 21)):
        print("from: %s, to: %s" % (state.reserved_from, state.reserved_to))
