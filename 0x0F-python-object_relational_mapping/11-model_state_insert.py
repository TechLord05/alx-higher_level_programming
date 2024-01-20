#!/usr/bin/python3
"""Module that adds the state Louisiana"""
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

    new_state = State(name='Louisiana')

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
