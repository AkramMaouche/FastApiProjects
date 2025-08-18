from fastapi import FastAPI 
import uvicorn

app = FastAPI()

@app.get("/users/{item_name}")
def road_user(item_name:str): 
    return {"user" : item_name}



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
#uvicorn app:app --reload