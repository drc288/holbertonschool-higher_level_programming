#!/usr/bin/python3
import sys
import sqlalchemy as db
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
"""
This script update data where id = 2 and change the
name to New Mexico
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
    # ---------CREATE-SESSION------------------
    Base.metadata.create_all(eng)
    new_session = sessionmaker(bind=eng)
    Session = new_session()
    # ------------------------------------------

    # Update the data
    query = Session.query(State). \
        filter(State.id == 2). \
        update({"name": ("New Mexico")})
    if query:
        Session.commit()
    else:
        Session.close()
