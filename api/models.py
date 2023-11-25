from pydantic import BaseModel , validator
from pymongo import MongoClient
from datetime import date

db = MongoClient("localhost:27017").pixel

class User(BaseModel):
    username: str 
    email: str 
    password: str
    @classmethod
    def create(self):
        print( "created")
        db.user.insert_one({'phraze':'jeez'})
    @validator("password")
    def validate_password_length(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value


class Patient(BaseModel):
    user_id: int
    addiction_score: int
    depression_score: int
    adhd_score: int
    insomnia_score: int

    @validator("addiction_score", "depression_score", "adhd_score", "insomnia_score")
    def validate_scores(cls, value):
        return cls.check_range(value)

class Doctor(BaseModel):
    user_id: int
    specialty: str 
    schedualed_sessions: int
    years_of_exp: int

class Admin(BaseModel):
    user_id: int
    admin_role: str
    permissions: int

class Quiz(BaseModel):
    patient_id: int
    quiz_date: date
    quiz_score: int

class Alert(BaseModel):
    patient_id: int
    alert_date: date
    alert_type: str

class Message(BaseModel):
    message_id: int
    sender_id: int
    receiver_id: int
    content: str
    message_date: date 

class UsageStats(BaseModel):
    stats_id: int
    user_id: int
    stats_date: date

class Token(BaseModel):
    access_token:str

class Login(BaseModel):
    email: str
    password:str