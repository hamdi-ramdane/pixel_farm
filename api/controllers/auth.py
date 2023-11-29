from fastapi import APIRouter
from pymongo import MongoClient
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from api.models import RegisterModel , LoginModel, LogoutModel
from pprint import pprint as print

db = MongoClient("localhost:27017").pixel

# Token Parameters 
def createToken(username):
    SECRET_KEY = "3f246e879f7ac59d822ff44015105939"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    token = jwt.encode({"username":username},key=SECRET_KEY,algorithm=ALGORITHM)
    db.token.insert_one({"token":token , "username":username})
    return token;
auth_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password Hasher
hasher = CryptContext(schemes=["bcrypt"],deprecated="auto")

router = APIRouter(prefix="/auth",tags=["Authentication"])
@router.post("/register")
def regiter(data : RegisterModel):
    new_user = {
        "username":data.username,
        "email":data.email,
        "password":hasher.hash(data.password),
        "is_verified":False,
    }
    db.user.insert_one(new_user)
    token = createToken(data.username)
    return {"status":True,"details":"Registration Successful","token":token}; 

@router.post("/login")
def login(data:LoginModel):
    user= db.user.find_one({"email": data.email})
    all = db.user.find()
    print(list(all))
    print(user)
    if not user or not hasher.verify(data.password,user.get("password")) :
        return {'status':False,'details':'invalid Credentials'} 
    token = createToken(user.get("username"))
    return {'status':True,'details':'Logged In Successfully',"token":token}

@router.post("/logout")
def logout(data :LogoutModel):
    result = db.token.delete_one({'token':data.token})
    if result.deleted_count == 0:
        return {'status':False,'details':'Token Invalid'}
    return {'status':True,'details':'Logged out Successfully'}
 