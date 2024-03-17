#!/usr/bin/python3

"""
8-model_state_fetch_first.py:
script that prints the first State object from the database hbtn_0e_6_usa
Usage: ./8-model_state_fetch_first.py <mysql username>
<mysql password> <database name>
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).first()

    if result:
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")

    session.close()
