# -*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from dao.config import DATABASE


def get_engine() -> Engine:
    return create_engine(URL(**DATABASE))

Base = declarative_base()

metadata = MetaData(bind=get_engine())
