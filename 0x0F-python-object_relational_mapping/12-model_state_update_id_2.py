#!/usr/bin/python3
"""module inserts state Louisiana into the db"""

import sys
from model_state import Base, State
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
    state_name = "New Mexico"

    state = sessn.query(State).get(2)
    state.name = state_name
    sessn.commit()

    sessn.close()
