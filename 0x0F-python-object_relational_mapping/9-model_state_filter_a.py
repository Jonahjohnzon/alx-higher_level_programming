#!/usr/bin/python3
""" print the first State object from database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()
    for i in sess.query(State).filter(State.name.like('%a%')):
        print(i.id, i.name, sep=": ")
