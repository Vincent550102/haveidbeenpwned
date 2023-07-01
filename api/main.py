from typing import Optional, Union
from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from pymongo import MongoClient
from routers import leak
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/version")
def read_version():
    return {"version": "0.0.8"}


@app.on_event("startup")
async def startup_event():
    mongo_username = os.getenv('MONGO_INITDB_ROOT_USERNAME', 'root')
    mongo_password = os.getenv('MONGO_INITDB_ROOT_PASSWORD', 'example')
    mongo_host = os.getenv('MONGO_HOST', 'mongo')
    app.state.db = MongoClient(
        f'mongodb://{mongo_username}:{mongo_password}@{mongo_host}:27017').leak
    print("connected to mongodb")


def get_db(app: FastAPI):
    return app.state.db


app.include_router(leak.router)
