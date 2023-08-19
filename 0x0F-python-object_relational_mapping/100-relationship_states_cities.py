#!/usr/bin/python3
"""module inserts state Louisiana into the db"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    uname = sys.argv[1]
    pswd = sys.argv[2]
    dname = sys.argv[3]
    conn_str = 'mysql+mysqldb://{}:{}@localhost/{}'.format(uname, pswd, dname)
    engn = create_engine(conn_str, pool_pre_ping=True)
    Base.metadata.create_all(engn)
    Session = sessionmaker(bind=engn)
    sessn = Session()
    state_name = "California"
    city_name = "San Francisco"

    state = State(name=state_name)
    city = City(name=city_name, state=state)
    state.cities.append(city)
    sessn.add(state)
    sessn.add(city)
    sessn.commit()

    sessn.close()
