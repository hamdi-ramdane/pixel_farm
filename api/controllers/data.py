from fastapi import APIRouter
from api.tools import db,authenticate
from typing import Annotated

router = APIRouter(prefix="/data",tags=['Data'])

@router.get('/pending')
def get_pending(username : Annotated[dict,authenticate]):
    result = db.pending.find({'username':username})
    return result

@router.get("/{table}")
async def getData( table:str):
    match table:
        case "user":
            return list(db.user.find({},{"_id":0}))
        case "patient":
            return list(db.patient.find({},{"_id":0}))
        case "doctor":
            return list(db.doctor.find({},{"_id":0}))
        case "admin":
            return list(db.admin.find({},{"_id":0}))
        case "quiz":
            return list(db.quiz.find({},{"_id":0}))
        case "message":
            return list(db.message.find({},{"_id":0}))
        case "alert":
            return list(db.alert.find({},{"_id":0}))
        case "usage":
            return list(db.usage.find({},{"_id":0}))
    return {
        'user' : "localhost:8000/data/user",
        'patient' : "localhost:8000/data/patient",
        'doctor' : "localhost:8000/data/doctor",
        'admin' : "localhost:8000/data/admin",
        'quiz' : "localhost:8000/data/quiz",
        'message' : "localhost:8000/data/message",
        'alert' : "localhost:8000/data/alert",
        'usage' : "localhost:8000/data/usage",
    } 