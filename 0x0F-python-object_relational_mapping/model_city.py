#!/usr/bin/python3

"""
Second state model
"""

from sqlalchemy import Column, VARCHAR, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()


class City(Base):
    """
    Class State inherits from Base
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(VARCHAR(128), nullable=False)
    state_id = Column(Integer, ForeignKey("State.id"), nullable=False)
