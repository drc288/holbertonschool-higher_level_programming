#!/usr/bin/python3
import sys
import sqlalchemy as db
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
"""
This script get all elements of the table argv[3]
"""


if __name__ == "__main__":
    # Get the data
    user = sys.argv[1]
    pswd = sys.argv[2]
    def_db = sys.argv[3]

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

    # Create the fist element
    first_obj = query.order_by(State.id).first()

    if first_obj:
        print("{}: {}".format(first_obj.id, first_obj.name))
    else:
        print("Nothing")
