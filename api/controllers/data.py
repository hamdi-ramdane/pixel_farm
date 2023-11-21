from fastapi import APIRouter

router = APIRouter()

@router.get("/data/{table}")
def register(table):
    return "Data : "+table

