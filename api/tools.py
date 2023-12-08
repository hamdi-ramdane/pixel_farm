from fastapi import HTTPException, Depends
from pymongo import MongoClient
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import datetime
from api.models import User
from pprint import pprint as print

db = MongoClient("localhost:27017").pixel

hasher = CryptContext(schemes=["bcrypt"],deprecated="auto")
# JWT TOKEN 
auth_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "3f246e879f7ac59d822ff44015105939"
ALGORITHM = "HS256"
def createToken(user:User):
    current_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    data_to_encode = {
        'username':user.username,
        'email':user.email,
        'perms':user.perms,
        'encoding_date':current_date
    }
    token = jwt.encode(data_to_encode,key=SECRET_KEY,algorithm=ALGORITHM)
    db.token.insert_one({"token":token , "username":user.username,'creation_date':current_date})
    return token;

def authenticate(token:str = Depends(auth_scheme)):
    token_exists = db.token.find_one({'token':token})
    if not token_exists:
        raise HTTPException(status_code=401,detail='Invalid Token')
    decoded_data = jwt.decode(token,key=SECRET_KEY,algorithms=[ALGORITHM])
    return User(**decoded_data)