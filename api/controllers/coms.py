from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from api.models import NotifyModel, MessageModel

auth_scheme = OAuth2PasswordBearer(tokenUrl='token')

router = APIRouter(prefix="/coms",tags=["Communication"])

@router.post("/message")
def message(data:MessageModel = Depends(auth_scheme)):
    return "Message sent";

@router.post("/notify")
def notify(data:NotifyModel = Depends(auth_scheme)):
    return "Notified";
