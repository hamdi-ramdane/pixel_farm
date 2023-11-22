from fastapi import APIRouter
from api.models import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

hasher = CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/register")
def register(username:str , password:str):

    return "Registered Fine"; 