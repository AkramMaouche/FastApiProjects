''' Create a basic FastAPI application
that sets up a SQLAlchemy engine and session,
defines a simple model for a "User" with id, name,
and email fields, and includes an endpoint to add a new user
to an in-memory SQLite database ''' 


import sqlalchemy 
from fastapi import FastAPI
from sqlalchemy import create_engine,Column,Integer,String, Boolean
from sqlalchemy.orm import Session,sessionmaker, declarative_base


#We're using an in-memory SQLite database for simplicity.
SQL_Alchemy_DAtabase_url = "sqlite:///:memory:"
app = FastAPI()



# Create Sql alchemy Engine 
engine =  create_engine(url= SQL_Alchemy_DAtabase_url, 
                        connect_args= {"check_same_thread":False}
                        )


# Create Session local Each instance of this class will be a
# database session. This is what we'll use to talk to the database.

SessionLocal = sessionmaker(autoflush=False ,bind=engine)

# `declarative_base` is the base class for our models.
# Our SQLAlchemy models will inherit from this class.

Base = declarative_base()


class User(Base): 
    __tablename__ = 'users' ## Create the table 
    id = Column(Integer, primary_key=True, index =True)
    name = Column(String, index=True)
    Email = Column(String, unique=True, index=True)



Base.metadata.create_all(bind=engine)




