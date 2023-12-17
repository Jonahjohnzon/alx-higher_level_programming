#!/usr/bin/python3
""" Creates State "California" with City "San Francisco" from a DB """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    sess = Session()

    State = State(name='California')
    City = City(name='San Francisco')
    State.cities.append(City)

    sess.add(State)
    sess.add(City)
    sess.commit()
