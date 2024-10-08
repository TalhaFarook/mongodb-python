# app.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import os

app = FastAPI()

# MongoDB connection details
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = os.getenv('MONGO_PORT', 27017)
mongo_uri = f'mongodb://{mongo_host}:{mongo_port}'

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client["test_database"]
collection = db["test_collection"]

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with MongoDB!"}

@app.post("/insert")
def insert_document():
    # Insert a test document
    collection.insert_one({"message": "Hello, MongoDB!"})
    return {"status": "Data inserted successfully"}

@app.get("/fetch")
def fetch_document():
    # Fetch and return inserted document
    doc = collection.find_one({"message": "Hello, MongoDB!"})
    if doc:
        return JSONResponse(content={"detail": doc['message']}, status_code = 200)
    else:
        return {"status": "Document not found"}