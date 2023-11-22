from fastapi import FastAPI, APIRouter
from api.controllers import data , auth

app = FastAPI()

app.include_router(data.router)
app.include_router(auth.router)

