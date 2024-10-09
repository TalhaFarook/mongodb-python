# app.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from routers.apis import apis_router
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials = True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(apis_router, prefix="/apis")

if __name__ == "__main__":
    uvicorn.run(app)