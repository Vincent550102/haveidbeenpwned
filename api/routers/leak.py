from starlette.requests import Request
from models import GetLeakRequest, GetLeakResponse, ErrorMessage
from fastapi import Depends, APIRouter, HTTPException
import hashlib
import pymongo

router = APIRouter()


def get_db(request: Request):
    return request.app.state.db


@router.get("/leak",
            status_code=200,
            responses={200: {"model": GetLeakResponse},
                       404: {"model": ErrorMessage}},
            tags=["currency"],
            summary="Get leaked columns",
            description="Get leaked columns by id_hash",
            deprecated=False)
def get_leaked_columns(id_number: str, db=Depends(get_db)):
    h = hashlib.new('sha256')
    h.update(id_number.encode('utf-8'))

    pipeline = [
        {"$unwind": "$data"},
        {"$group": {
            "_id": "$data.身份證字號",
            "matched_data": {"$push": "$data"},
            "name": {"$first": "$name"}
        }},
        {"$match": {"_id": h.hexdigest()}}
    ]
    leaked = db.fakedata.aggregate(pipeline)

    # leaked = db.fakedata.find_one({"data.身份證字號": h.hexdigest()})
    leaked = list(leaked)
    print(leaked)
    result = []
    if len(leaked):
        result.append({
            "name": leaked[0]["name"],
            "data": list(leaked[0]["matched_data"][0].keys())
        })
    return {
        "leaks": result
    }
