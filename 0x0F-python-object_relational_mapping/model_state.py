#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
"""
Sate - create a new table states and add the property
id and name
"""


class State(Base):
    """ Popertys of clas State: id and name """
    # Declare the name of the table
    __tablename__ = 'states'

    # Create the proprties id and name
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
