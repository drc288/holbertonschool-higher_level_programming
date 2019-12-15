#!/usr/bin/python3
import sys
import sqlalchemy as db
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
"""
Delete all records of the table states with contain the letter a
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

    # Get the query
    query = Session.query(State, City)
    # Get the relational data
    relational = query.filter(State.id == City.state_id).\
        order_by(City.id).all()

    for data_state, data_city in relational:
        print("{}: ({}) {}".format(data_state.name,
                                   data_city.id,
                                   data_city.name))
