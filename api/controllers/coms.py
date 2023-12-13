from fastapi import APIRouter, Depends,HTTPException
from api.models import NotificationModel, MessageModel
from api.tools import db,authenticate
from typing import Annotated
from datetime import datetime
from api.models import User
router = APIRouter(prefix="/coms",tags=["Communication"])

@router.post("/message")
async def message(user: Annotated[User,Depends(authenticate)],data:MessageModel):
    receiver_exists = db.user.find_one({'username':data.receiver_username})
    if not receiver_exists:
        raise HTTPException(status_code=400,detail="Receiver Does Not Exist")

    message = {
        'sender':user.username,
        'receiver':data.receiver_username,
        'content':data.content,
        'sent_at':datetime.now().strftime("%d-%m-%Y %H:%M")
    }
    msg_id = db.message.insert_one(message).inserted_id
    db.pending.insert_one({'type':'message',"msg_id":msg_id,})
    return {'detail':"Message sent Successfully"};

@router.post("/notification")
async def notification(user: Annotated[User,Depends(authenticate)],data:NotificationModel):

    #check if doctor or above (permissions)
    if(user.perms<4):
        raise HTTPException(status_code=400,detail='Permission Denied')
    
    #check notification receiver exists 
    receiver_exists = db.user.find_one({'username':data.receiver_username})
    if not receiver_exists:
        raise HTTPException(status_code=400,detail="Receiver Does Not Exist")

    notification = {
        'sender':user.username,
        'receiver':data.receiver_username,
        'content':data.content,
        'sent_at':datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    not_id= db.notification.insert_one(notification).inserted_id
    db.pending.insert_one({'type':'notification',"not_id":not_id,})
    return {'detail':"Notification Sent Successfully"};

# 1 1 1 1 1 = super_admin | admin | doctor | verified_byEmail | Activated (not disabled)

