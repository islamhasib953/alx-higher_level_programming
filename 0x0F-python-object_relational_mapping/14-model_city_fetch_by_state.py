#!/usr/bin/python3


"""
14-model_city_fetch_by_state.py:
script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa
Usage: ./14-model_city_fetch_by_state.py <mysql username>
<mysql password> <database name>
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )
    for r in res:
        print("{}: ({}) {}".format(r.State.name, r.City.id, r.City.name))

    session.commit()

    session.close()
