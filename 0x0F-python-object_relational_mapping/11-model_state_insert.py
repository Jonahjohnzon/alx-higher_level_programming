#!/usr/bin/python3
""" print State object with name passed as argument from database"""
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
    _state = State(name='Louisiana')
    sess.add(_state)
    _instance = sess.query(State).filter_by(name='Louisiana').first()
    print(_instance.id)
    sess.commit()
