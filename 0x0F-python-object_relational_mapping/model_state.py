# #!/usr/bin/python3

# """
# First state model
# """

# from sqlalchemy import create_engine, Column, Integer, VARCHAR
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()


# class State(Base):
#     """
#     Class State inherits from Base
#     """

#     __tablename__ = "states"
#     id = Column(Integer(11), primary_key=True, autoincrement=True, nullable=False)
#     name = Column(VARCHAR(128), nullable=False)


#!/usr/bin/python3
"""
base srate model class for the project
"""

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, VARCHAR, Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
