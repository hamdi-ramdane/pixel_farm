from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login(email: str ,password: str):
    return "Logged In fine"