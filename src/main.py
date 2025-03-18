from fastapi import FastAPI, UploadFile
from src.transcription_model import transcribe_file
from typing import Annotated

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    response = await transcribe_file(file.file)
    return {"transcription": response}
