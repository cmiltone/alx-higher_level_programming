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

    q = sessn.query(State).order_by(State.id)

    j = 1
    for state in q:
        # q2 = sessn.query(City).filter(City.state_id==state.id)

        for city in state.cities:
            print("{}: {} -> {}".format(j, city.name, state.name))
            j += 1

    sessn.close()
