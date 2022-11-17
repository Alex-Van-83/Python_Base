from fastapi import APIRouter
import json
router = APIRouter(
    tags=["Users"],
)

local_storage = dict()


@router.get("/ping/")
def ping():
    return {"message": "pong"}


@router.get("/{key}")
def value(key: str):

    data = local_storage.get(key)

    return {"key": key,
            "value": data,
            }


@router.post("/{key}")
def include_data(key:str, data:str):
    local_storage[key] = data
    return {key}

