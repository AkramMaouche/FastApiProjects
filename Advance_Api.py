from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
import pydantic
from typing import List


app = FastAPI()

@app.post("/login")
async def login(name:str = Form(...), password:str = Form(...)): 
    return {"username": name, "message": "Login successfuly"}

@app.post("/upload")
async def Upload_file(file: UploadFile = File(...)):
    return {"file Name": file.filename}

@app.post("/Save_upload")
async def save_upload(file: UploadFile = File(...)):
    with open(f"Uploads/{file.filename}",'wb')as F : 
        F.write(file.file.read())
    return {"messege": f"File'{file.filename}' saved successfully"}

@app.post("/Multiple_uploads")
async def Upload_file(files: List[UploadFile] = File(...)):
    return {"file Names": [file.filename for file in files]}



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn Advance_Api:app --reload


