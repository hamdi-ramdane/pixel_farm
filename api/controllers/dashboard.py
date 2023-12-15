from fastapi import APIRouter, Depends, HTTPException
from api.models import User,UpdateProfileModel,BanUserModel,DeleteUserModel,GrantAdminModel
from api.tools import db, authenticate
from typing import Annotated


router = APIRouter(prefix="/dashboard",tags=["Dashboard"])

@router.post('/update-profile')
async def update_profile(user: Annotated[User,Depends(authenticate)],data:UpdateProfileModel):
    updated_fields = dict(data)
    updated_fields['date_of_birth'] =  updated_fields['date_of_birth'].strftime("%Y-%m-%d")
    db.user.update_one({'username':user.username},{'$set': updated_fields})
    return {"detail":"Profile Updated Successfully"}

@router.post("/ban-user")
async def ban_user(user : Annotated[User, Depends(authenticate)],data:BanUserModel):
    if user.perms < 8 :
        raise HTTPException(status_code=400,detail="Permission Denied")

    current_perms = db.user.find_one({'username':data.username},{'perms'})
    if not current_perms:
        raise HTTPException(status_code=400,detail="User Does Not Exist")

    current_perms = current_perms['perms']
    updated_perms = current_perms - 1 if current_perms%2 == 1 else current_perms

    db.user.update_one({'username':data.username},{'$set':{'perms':updated_perms}})
    return {"detail":"User Banned Successfully"}

@router.post("/delete-user")
async def delete_user(user : Annotated[User, Depends(authenticate)],data:DeleteUserModel):
    if user.perms < 8 :
        raise HTTPException(status_code=400,detail="Permission Denied")


    delete_result = db.user.delete_one({'username':data.username})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=400,detail="User Does Not Exist")
    return {"detail":"User Deleted Successfully"}

@router.post('/grant-admin')
async def grant_admin(user: Annotated[User,Depends(authenticate)],data:GrantAdminModel):
    if user.perms < 16 :
        raise HTTPException(status_code=400,detail="Permission Denied")

    current_perms = db.user.find_one({'username':data.username},{'perms'})

    if not current_perms:
        raise HTTPException(status_code=400,detail="User Does Not Exist")

    current_perms = current_perms['perms']
    updated_perms = current_perms + 8 if current_perms < 8 else current_perms
    if current_perms == updated_perms:
        return {"detail":"Admin Granted"}

    db.user.update_one({'username':data.username},{'$set':{'perms':updated_perms}})
    db.admin.insert_one({'username':data.username,'role':'moderator'})
    return {"detail":"Admin Granted"}
