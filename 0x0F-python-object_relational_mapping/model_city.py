#!/usr/bin/python3
"""
from input
"""
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from model_state import *


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
