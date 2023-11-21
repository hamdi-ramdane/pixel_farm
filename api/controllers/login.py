from fastapi import APIRouter

router = APIRouter()

@router.get("/login")
def login():
    return "Logged In fine"

@router.post("/login")
def login():
    return "Logged In fine"