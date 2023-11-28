from fastapi import APIRouter
from api.models import NotifyModel, MessageModel

router = APIRouter(prefix="/coms",tags=["Communication"])

@router.post("/message")
def notify(data:MessageModel):
    return "Message sent";

@router.post("/notify")
def notify(data:NotifyModel):
    return "Notified";
