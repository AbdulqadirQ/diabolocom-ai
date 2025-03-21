from fastapi import FastAPI, UploadFile
from src.statistics_db import add_call, language_of_calls, \
    number_of_calls, median_call_duration, median_call_latency
from src.transcription_model import transcribe_file

app = FastAPI()

# EXPLANATION: each endpoint refers to the releant module and function
#              The responses are not wrapped in a data structure, rather given back to the user
#              in a format that'd be most useful to them
@app.get("/statistics/language_of_calls")
def get_language_of_calls():
    return language_of_calls()

@app.get("/statistics/number_of_calls")
def get_number_of_calls():
    return number_of_calls()

@app.get("/statistics/median_call_duration")
def get_median_call_duration():
    return f"{median_call_duration()} seconds"

@app.get("/statistics/median_call_latency")
def get_median_call_duration():
    return f"{median_call_latency()} ms"

@app.post("/upload_call/")
async def create_upload_file(file: UploadFile):
    model_result = await transcribe_file(file.file)
    # EXPLANATION: each call's data is recorded within the database
    add_call(model_result["language"], model_result["duration"], model_result["latency"])
    return {"transcription": model_result["transcription"]}
