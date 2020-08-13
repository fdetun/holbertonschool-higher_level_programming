#!/usr/bin/python3
"""fetchall"""


from sqlalchemy import create_engine
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    request = "mysql+mysqldb://{}:{}@localhost:3306/{}\
    ".format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(request, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in session.query(State).order_by(State.id).all():
        print("{}: {}".format(i.id, i.name))
    session.close()
