#!/usr/bin/python3
"""fetchall"""
from sqlalchemy import *
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

request = "mysql+mysqldb://{}:{}@localhost/{}\
".format(sys.argv[1], sys.argv[2], sys.argv[3])
engine = create_engine(request, pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
for i in session.query(State).order_by(State.id):
    print(i.id, end=': ')
    print(i.name)
session.close()
