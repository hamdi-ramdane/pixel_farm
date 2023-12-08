from fastapi import APIRouter, Depends
from api.models import BanModel,User
from api.tools import db, authenticate
from typing import Annotated


router = APIRouter(prefix="/dashboard",tags=["Dashboard"])

@router.post("/ban")
def ban(data : Annotated[BanModel , Depends(authenticate)]):
    return "Banned"
@router.post('/updateprofile')
def update_profile(user: Annotated[User,authenticate]):
    return "updated"

