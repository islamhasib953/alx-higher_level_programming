#!/usr/bin/python3

"""
10-model_state_my_get.py:
Script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password>
<database name> <state name searched>
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

    result = session.query(State).filter_by(name=argv[4]).all()

    if result:
        for record in result:
            print("{}".format(record.id))
    else:
        print("Not found")

    session.close()
