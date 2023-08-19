#!/usr/bin/python3
"""module uses State model to list states"""

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
    state = sessn.query(State).order_by(State.id).first()
    print('{}: {}'.format(state.id, state.name))

    sessn.close()
