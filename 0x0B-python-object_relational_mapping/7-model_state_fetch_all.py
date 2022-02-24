#!/usr/bin/python3
"""Uses ORM sqlalchemy to all State objects from db hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    '''should not execute when imported'''

    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print(f'{state.id}: {state.name}')
    session.close()

if __name__ == "__main__":
    main()
