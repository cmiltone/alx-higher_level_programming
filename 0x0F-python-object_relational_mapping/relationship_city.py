#!/usr/bin/python3
"""module defines City class for city model"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """class for city model"""
    __tablename__ = 'cities'
    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        unique=True,
        autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
