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
    search = sys.argv[4]
    found = False
    for state in sessn.query(State).filter(State.name == search):
        print('{}'.format(state.id))
        found = True
    if found is False:
        print("Not found")

    sessn.close()
