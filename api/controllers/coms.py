from fastapi import APIRouter, Depends,HTTPException
from api.models import NotificationModel, MessageModel
from api.tools import db,authenticate
from typing import Annotated
from datetime import datetime
from api.models import User
router = APIRouter(prefix="/coms",tags=["Communication"])

@router.post("/message")
async def send_message(user: Annotated[User,Depends(authenticate)],data:MessageModel):
    receiver_exists = db.user.find_one({'username':data.receiver_username})
    if not receiver_exists:
        raise HTTPException(status_code=400,detail="Receiver Does Not Exist")
    if data.receiver_username == user.username:
        raise HTTPException(status_code=400,detail="User Cannot Send a message to himself")
    message = {
        'sender':user.username,
        'receiver':data.receiver_username,
        'content':data.content,
        'sent_at':datetime.now().strftime("%d-%m-%Y %H:%M")
    }
    db.message.insert_one(message)
    message['type']='message'
    db.pending.insert_one(message)
    return {'detail':"Message sent Successfully"};

@router.post("/notification")
async def send_notification(user: Annotated[User,Depends(authenticate)],data:NotificationModel):

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

    db.notification.insert_one(notification)
    notification['type']='notification'
    db.pending.insert_one(notification)
    return {'detail':"Notification Sent Successfully"};

@router.get('/pending/{type}')
async def pending_messages_and_notifications(user : Annotated[User,Depends(authenticate)],type:str):
    if type.lower() not in ['message','notification']:
        raise HTTPException(status_code=400,detail="Invalid Endpoint , /message or /notification")
    pending = list(db.pending.find({'receiver':user.username,'type':type},{'_id':0}))
    return pending 

@router.post('/pending-read/{type}')
async def read_pending(user : Annotated[User,Depends(authenticate)],type:str):
    if type.lower() not in ['message','notification']:
        raise HTTPException(status_code=400,detail="Invalid Endpoint , /message or /notification")
    db.pending.delete_many({'receiver':user.username,'type':type})
    return {'detail':'Pending '+type+'s Have been read'} 

@router.get('/history/{type}')
async def message_and_notifcation_history(user : Annotated[User,Depends(authenticate)],type:str):
    if type.lower() not in ['message','notification']:
        raise HTTPException(status_code=400,detail="Invalid Endpoint , /message or /notification")
    if type.lower() == 'message':
        result = list(db.message.find({'receiver':user.username},{'_id':0}))
    else :
        result = list(db.notification.find({'receiver':user.username},{'_id':0}))
    return result




