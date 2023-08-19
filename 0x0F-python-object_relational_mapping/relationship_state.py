#!/usr/bin/python3
"""module defines class State"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """class for state model"""
    __tablename__ = 'states'
    id = Column(
        Integer,
        unique=True,
        nullable=False,
        autoincrement=True,
        primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')
