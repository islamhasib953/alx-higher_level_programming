#!/usr/bin/python3

"""
First state model
"""

from sqlalchemy import create_engine, Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    Class State inherits from Base
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(VARCHAR(128), nullable=False)
