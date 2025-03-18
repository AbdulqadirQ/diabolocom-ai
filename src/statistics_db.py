import os
import pymongo
from collections import Counter

hostname = os.environ["MONGO_INITDB_HOSTNAME"]
username = os.environ["MONGO_INITDB_ROOT_USERNAME"]
password = os.environ["MONGO_INITDB_ROOT_PASSWORD"]

mongo_client = pymongo.MongoClient(hostname, username=username, password=password)

db = mongo_client["statistics"]
statistics_collection = db["statistics_collection"]

def add_call(language, duration, latency):
    call = {"language": language, "latency": latency, "audio_length": duration}
    print(call)
    statistics_collection.insert_one(call)

def language_of_calls():
    list_of_languages = []
    for call in statistics_collection.find():
        list_of_languages.append(call["language"])
    return Counter(list_of_languages)

def number_of_calls():
    return statistics_collection.count_documents({})

def median_call_duration():
    sum_of_audio_length = 0
    for call in statistics_collection.find():
        sum_of_audio_length += int(call["audio_length"])
    return round(sum_of_audio_length / number_of_calls(), 2)

def median_call_latency():
    sum_of_latency = 0
    for call in statistics_collection.find():
        sum_of_latency += int(call["latency"])
    return round(sum_of_latency / number_of_calls(), 2)
