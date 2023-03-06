from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Executing instructions from the chinnok database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# Create class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# Create a new instance of sessionmaker, then point it to our engine (db)
Session = sessionmaker(db)
# Open the session by calling the Session subclass defined above
session = Session()

# Create the database using the declaritive_base subclass
base.metadata.create_all(db)


# Creating records on our Programmers table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="Brtish",
    famous_for="First Programmer"
)
