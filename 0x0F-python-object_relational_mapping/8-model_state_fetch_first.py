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
    first = session.query(State).order_by(State.id).first()
    if first is None:
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))
    session.close()
