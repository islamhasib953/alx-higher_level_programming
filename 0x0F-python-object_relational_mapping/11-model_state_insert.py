#!/usr/bin/python3


"""
11-model_state_insert.py:
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
Usage: ./3-my_safe_filter_states.py <mysql username>
<mysql password> <database name>
"""


from sqlalchemy import create_engine
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
    insert = State(name="Louisiana")
    session.add(insert)

    session.commit()
    print(insert.id)

    session.close()
