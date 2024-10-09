import pymongo, os
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from datetime import datetime

apis_router = APIRouter()

# MongoDB connection details
mongo_host = os.getenv('MONGO_HOST', 'localhost')
mongo_port = os.getenv('MONGO_PORT', 27017)
mongo_uri = f'mongodb://{mongo_host}:{mongo_port}'

# Connect to MongoDB
client = MongoClient(mongo_uri)
db = client["test_database"]
collection = db["test_collection"]

@apis_router.get('/')
def read_root():
    return {"message": "Welcome to FastAPI with MongoDB!"}

@apis_router.get('/new')
def read_root():
    return {"message": "This is the new API you were hoping for!"}

@apis_router.post('/insert')
def insert_document():
    collection.insert_one({"message": "Hello, MongoDB!"})
    return {"status": "Data inserted successfully"}

@apis_router.get('/fetch')
def fetch_document():
    doc = collection.find_one({"message": "Hello, MongoDB!"})
    if doc:
        return JSONResponse(content={"detail": doc['message']}, status_code = 200)
    else:
        return {"status": "Document not found"}