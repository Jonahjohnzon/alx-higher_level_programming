#!/usr/bin/python3
""" prints  State object with  name passed as argument from database """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                         .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()
    for ins in sess.query(State).order_by(State.id):
        print(ins.id, ins.name, sep=": ")
        for city_ins in ins.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
