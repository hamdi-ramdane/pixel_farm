from fastapi import FastAPI, APIRouter
from api.controllers import data , register , login

app = FastAPI()

app.include_router(data.router)
app.include_router(register.router)
app.include_router(login.router)

