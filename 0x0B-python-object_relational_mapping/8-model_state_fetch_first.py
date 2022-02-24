#!/usr/bin/python3
"""Uses ORM sqlalchemy to print the first State object from db hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def main():
    '''should not execute when imported'''

    engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if state:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')

if __name__ == "__main__":
    main()
