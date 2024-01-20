#!/usr/bin/python3
"""Module that prints the updates the state name based on filtered id"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    conn_url = "mysql://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])
    engine = create_engine(conn_url, pool_pre_ping=True)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name.contains('a')).all()

    for s in state:
        session.delete(s)

    session.commit()
    session.close()
