from fastapi import APIRouter
from api.models import BanModel
router = APIRouter(prefix="/admin",tags=["Admin"])

@router.post("/ban")
def ban(data : BanModel):
    return "Banned"
    