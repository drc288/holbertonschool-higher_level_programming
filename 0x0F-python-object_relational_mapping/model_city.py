#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
"""
Sate - create a new table states and add the property
id and name
"""


class City(Base):
    """ Popertys of clas State: id and name """
    # Declare the name of the table
    __tablename__ = 'cities'

    # Create the proprties id and name and the foreign key
    id = Column(Integer,
                primary_key=True,
                unique=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey("state.id"),
                      nullable=False)
