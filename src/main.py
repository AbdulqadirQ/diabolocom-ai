import transcription_model
from fastapi import FastAPI, UploadFile
from typing import Annotated


app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
