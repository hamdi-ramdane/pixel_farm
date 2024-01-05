from fastapi import APIRouter,Depends
from api.models import QuizSubmitModel, User
from api.tools import db,authenticate
from typing import Annotated
from datetime import datetime

router = APIRouter(prefix="/data",tags=["Data"])
@router.get("/allusers")
async def get_all_usernames():
    users = list(db.user.find({},{'username':1,'perms':1,'_id':0}))
    for user in users:
        if user['perms'] > 4 :
            user['user_type'] = 'doctor';
        else:
            user['user_type'] = 'patient'
        user.pop('perms')
    return users

@router.get("/user")
async def get_user_info(user : Annotated[User,Depends(authenticate)]):
    username = user.username
    user_in_db = db.user.find_one({'username':username},{'_id':0,'hashed_password':0})
    return dict(user_in_db)
    