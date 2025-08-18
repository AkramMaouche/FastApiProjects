from fastapi import FastAPI 
import uvicorn 
from pydantic import BaseModel, Field , field_validator



app = FastAPI() 

class User(BaseModel):
    user_name:str 
    age:int = Field(...,ge= 20, le=35)

    @field_validator("user_name")
    def name_must_not_beempty(cls, v): 
        if not v: 
            raise ValueError ("name must be not empty")
        return v 


@app.post("/users/")
def create_user(user:User):
    return {"user": user.user_name, "age": user.age}




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn Main_Pydantic:app --reload