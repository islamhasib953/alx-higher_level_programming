#!/usr/bin/python3

"""
9-model_state_filter_a.py:
script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
Usage: ./9-model_state_filter_a.py <mysql username>
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

    result = session.query(State).filter(State.name.like("%a%")).all()

    for record in result:
        print("{}: {}".format(record.id, record.name))

    session.close()
