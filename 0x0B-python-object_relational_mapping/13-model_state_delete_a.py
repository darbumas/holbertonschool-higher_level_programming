#!/usr/bin/python3
"""Deletes any State obj containing a letter "a" to db hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    '''should not execute when imported'''

    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
