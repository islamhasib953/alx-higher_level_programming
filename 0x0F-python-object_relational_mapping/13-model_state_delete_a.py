#!/usr/bin/python3


"""
13-model_state_delete_a.py:
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
Usage: ./13-model_state_delete_a.py <mysql username>
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

    delete = session.query(State).filter_by(name="%a%").all()
    if delete:
        for res in delete:
            session.delete(res)

    session.commit()

    session.close()
