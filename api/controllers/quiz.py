
from fastapi import APIRouter,Depends
from api.models import QuizSubmitModel, User
from api.tools import db,authenticate
from typing import Annotated
from datetime import datetime


router = APIRouter(prefix="/quiz",tags=["Quiz"])
@router.post("/submit")
async def submit_quiz(user : Annotated[User,Depends(authenticate)],data:QuizSubmitModel):
    result = dict(data)
    result['username'] = user.username
    result['submited_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.quiz.insert_one(result)
    return {'detail':'Quiz Submited Successfully'} 

@router.get('/history')
async def quiz_history(user: Annotated[User,Depends(authenticate)]):
    result = list(db.quiz.find({'username':user.username},{'_id':0}))
    return result