from fastapi import APIRouter
from api.models import User

router = APIRouter()

@router.get("/register")
def register():
    user = User(
        first_name="morty",
        last_name="smith",
        username="morty_smith",
        gender="Male",
        date_of_birth="2023-01-01",
        email="smashyomum@gmail.com",
        password="randomapssword123"
    )
    User.create()
    return user; 

@router.post("/register")
def register(user: User):
    return "Registered Fine"; 