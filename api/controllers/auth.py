from fastapi import APIRouter, HTTPException, Depends
from api.tools import createToken,hasher,auth_scheme, db
from api.models import RegisterModel , LoginModel ,User
from pprint import pprint as print
from typing import Annotated


router = APIRouter(prefix="/auth",tags=["Authentication"])

@router.post("/register")
async def regiter(data : RegisterModel):
    new_user = {
        "username":data.username,
        "email":data.email,
        "hashed_password":hasher.hash(data.password),
        "gender":data.gender,
        "date_of_birth":data.date_of_birth
    }
    
    if data.user_type.lower() == 'patient':
        db.patient.insert_one({'username':data.username})
        new_user['perms'] = 1
    else:
        db.doctor.insert_one({'username':data.username})
        new_user['perms'] = 5

    db.user.insert_one(new_user)
    token = createToken(User(
        username=data.username,
        email=data.email,perms=new_user['perms']
        )
    )

    return {"details":"Registration Successful","token":token}; 

@router.post("/login")
async def login(data:LoginModel):
    user= db.user.find_one({"email": data.email})
    if not user or not hasher.verify(data.password,user.get("hashed_password")) :
        raise HTTPException(status_code=400,detail='invalid Credentials')
    token = createToken(User(
        username=user.get('username'),
        email=user.get('email'),
        perms=user.get('perms')
        )
    )
    return {'details':'Logged In Successfully',"token":token}

@router.post("/logout")
async def logout(token: Annotated[LoginModel,Depends(auth_scheme)]):
    delete_result = db.token.delete_many({'token':token})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=401,detail='Invalid Token')
    return {'details':'Logged out Successfully'}
 