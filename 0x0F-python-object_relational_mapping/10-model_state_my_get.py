#!/usr/bin/python3
"""fetchall"""


from sqlalchemy import create_engine
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    request = "mysql+mysqldb://{}:{}@localhost:3306/{}".\
        format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(request, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    f = session.query(State).filter(State.name == sys.argv[4]).first()
    if f:
        print(f.id)
    else:
        print("Not found")
    session.close()
