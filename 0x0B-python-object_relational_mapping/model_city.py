#!/usr/bin/python3
"""Creates a class 'City' and an instance -> Base = declarative_base()"""
from sqlalchemy import Column, Integer, String
from model_state import Base, State
from sqlalchemy.sql.schema import ForeignKey


class City(Base):
    '''child class of Base'''

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
