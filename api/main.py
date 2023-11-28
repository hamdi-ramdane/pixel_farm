from fastapi import FastAPI, APIRouter
from api.controllers import data , auth, coms, admin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data.router)
app.include_router(auth.router)
app.include_router(coms.router)
app.include_router(admin.router)

