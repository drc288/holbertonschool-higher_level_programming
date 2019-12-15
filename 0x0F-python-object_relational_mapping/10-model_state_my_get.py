#!/usr/bin/python3
import sys
import sqlalchemy as db
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
"""
This script get all elements and filter wiht a
"""


if __name__ == "__main__":
    # Get the data
    user = sys.argv[1]
    pswd = sys.argv[2]
    def_db = sys.argv[3]
    state_n = sys.argv[4]

    # Create the connection
    eng = db.create_engine(
        'mysql+mysqldb://{:s}:{:s}@localhost/{:s}'
        .format(user, pswd, def_db)
    )

    # Create the metadata of the connection eng
    Base.metadata.create_all(eng)
    new_session = sessionmaker(bind=eng)
    Session = new_session()
    query = Session.query(State)

    # Filter the data
    # PSDT = SQLAlchemy prevent automatly SQL injections
    filter = query.\
        filter(State.name == state_n).\
        order_by(State.id).all()

    if filter:
        print(filter[0].id)
    else:
        print("Not found")
