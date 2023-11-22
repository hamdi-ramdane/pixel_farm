from fastapi import APIRouter

router = APIRouter()

@router.post("/login",tags=["Authentication"])
def login(email: str ,password: str):
    return "Logged In fine"