from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from api.models import BanModel

auth_scheme = OAuth2PasswordBearer(tokenUrl='token')

router = APIRouter(prefix="/admin",tags=["Admin"])

@router.post("/ban")
def ban(data : BanModel = Depends(auth_scheme)):
    return "Banned"
    