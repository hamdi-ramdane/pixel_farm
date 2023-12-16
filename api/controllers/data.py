from fastapi import APIRouter,Depends
from api.models import QuizSubmitModel, User
from api.tools import db,authenticate
from typing import Annotated
from datetime import datetime

router = APIRouter(prefix="/data",tags=["Data"])
@router.get("/usernames")
async def get_all_usernames():
    usernames = list(db.user.find({},{'username':1,'_id':0}))
    print(usernames)
    return usernames
