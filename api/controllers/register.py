from fastapi import APIRouter
from api.models import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from pymongo import MongoClient

router = APIRouter()

db = MongoClient("localhost:27017").pixel

hasher = CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@router.post("/register",tags=["Authentication"])
def register(username:str , password:str):
    new_user = {
        "username" :username,
        "password": "gay"
    }
    db.user.insert_one(new_user)
    return "Registered Fine"; 