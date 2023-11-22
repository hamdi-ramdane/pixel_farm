from fastapi import APIRouter
from passlib.context import CryptContext
from api.models import User
from fastapi.security import OAuth2PasswordBearer
from pymongo import MongoClient


db = MongoClient("localhost:27017").pixel

hasher = CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(username: str):
    user_data = db.user.find_one({"username": username})
    if user_data:
        return {'username':username , 'password':user_data['password']}

router = APIRouter()
@router.post("/register",tags=["Authentication"])
def register(username:str , email:str, password:str):
    new_user = {
        "username":username,
        "email":email,
        "password":password
    }
    db.user.insert_one(new_user)
    return {"status":True,"details":"Registration Successful"}; 

@router.post("/login",tags=["Authentication"])
def login(username: str ,password: str):
    user = get_user(username)
    if not user or not hasher.verify(password,user["password"]) :
        return {'status':False,'details':'invalid Credentials'} 
    return {'status':True,'details':'Logged In Successfully'}

@router.post("/logout",tags=["Authentication"])
def logout(token:str="default"):
    return {'status':True,'details':'Logged out Successfully'}