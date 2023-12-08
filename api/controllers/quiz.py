
from fastapi import APIRouter,Depends
from api.models import QuizSubmitModel, User
from api.tools import db,authenticate
from typing import Annotated

router = APIRouter(prefix="/quiz",tags=["Quiz"])
@router.post("/submit")
def submit(user : Annotated[User,Depends(authenticate)],data:QuizSubmitModel):
    return "quiz submited"

@router.get("/history")
def user_quiz_history(user : Annotated[User,Depends(authenticate)]):
    return "retreived "