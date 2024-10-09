# app.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
from routers.apis import apis_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials = True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(apis_router, prefix="/apis")