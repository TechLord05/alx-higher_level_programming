#!/usr/bin/python3
"""Module that lists all State objects that contain the letter a"""
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

    states = session.query(State).order_by(State.id).all()

    for state in states:
        if ("a" in state.name):
            print("{}: {}".format(state.id, state.name))

    session.close()
