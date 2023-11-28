from fastapi import APIRouter
from pymongo import MongoClient
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from api.models import RegisterModel , LoginModel, LogoutModel

SECRET_KEY = "3f246e879f7ac59d822ff44015105939"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

db = MongoClient("localhost:27017").pixel
hasher = CryptContext(schemes=["bcrypt"],deprecated="auto")
auth_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user(email: str):
    user_data = db.user.find_one({"email": email})
    if user_data:
        return {'email':email, 'password':user_data['password']}

router = APIRouter(prefix="/auth",tags=["Authentication"])
@router.post("/register")
def register(data : RegisterModel):
    new_user = {
        "username":data.username,
        "email":data.email,
        "password":hasher.hash(data.password)
    }
    print(new_user["password"])
    db.user.insert_one(new_user)
    return {"status":True,"details":"Registration Successful"}; 

@router.post("/login")
def login(data:LogoutModel):
    user = get_user(data.email)
    if not user or not hasher.verify(data.password,user["password"]) :
        return {'status':False,'details':'invalid Credentials'} 
    return {'status':True,'details':'Logged In Successfully'}

@router.post("/logout")
def logout(data :LogoutModel):
    return {'status':True,'details':'Logged out Successfully'}