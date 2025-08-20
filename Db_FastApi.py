from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.ext.declarative  import declarative_base 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import Session 
from pydantic import BaseModel

from fastapi import FastAPI, Depends

from Main_Pydantic import User
app = FastAPI() 


DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args = {"check_same_thread": False})

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine) 

Base = declarative_base()



def get_db(): 
    db = SessionLocal()
    try: 
        yield db  # return a value then stop the function 
    finally: 
        db.close()



class UserCreate(BaseModel): 
    name: str 
    email: str

class UserResponse(BaseModel): 
    __tablename__ = "users" 

    id : int    
    name : str
    email : str

    class Config:
        orm_mode = True



@app.post("/users/", response_model = UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)): 
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



#uvicorn Db_FastApi:app --reload