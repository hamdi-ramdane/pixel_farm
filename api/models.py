from pydantic import BaseModel , validator, EmailStr
from pymongo import MongoClient
from datetime import date,datetime
from re import match

db = MongoClient("localhost:27017").pixel

class User(BaseModel):
    username: str
    email: EmailStr 
    perms:int = 1

# Authentication =========================================================
# ========================================================================
class RegisterModel(BaseModel):
    username: str
    email: EmailStr
    password: str = 'password123' # -----------------------------------------------------------
    gender: str = "male"
    date_of_birth: date = date(2005,3,25)
    user_type: str = 'patient'
    @validator('username')
    def check_unique_username(cls,value):
        if db.user.find_one({"username":value}):
            raise ValueError("Username Taken")
        if not match(r'^[a-z0-9_]+$', value):
            raise ValueError("Invalid username format. It should contain only letters, numbers, lowercase letters, and underscores.")
        return value
    @validator('email')
    def check_unique_email(cls,value):
        if db.user.find_one({"email":value}):
            raise ValueError("Email Already Used")
        return value 
    @validator("password")
    def check_length_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value
    @validator("user_type")
    def check_user_type(cls,value):
        if value.lower() not in ["doctor","patient"]:
            raise ValueError("Invalid User Type [doctor, patient]")
        return value
    @validator("gender")
    def check_gender(cls,value):
        if value.lower() not in ["male","female"]:
            raise ValueError("Invalid Gender [Male, Female]")
        return value
    @validator("date_of_birth")
    def check_date_of_birth(cls,value):
        age = datetime.now().date().year - value.year
        if age < 13:
            raise ValueError("Too Young (must be 13 or above)")
        elif age > 100 :
            raise ValueError("Too Old (must be less than a 100 y/o) ")
        
        return value

class LoginModel(BaseModel):
    email:str
    password:str = 'password123' # ------------------------------------------------------------

# Communication ==========================================================
# ========================================================================
class MessageModel(BaseModel):
    receiver_username:str
    content:str

class NotificationModel(BaseModel):
    receiver_username:str
    content:str

# Admin ==================================================================
# ========================================================================
class BanModel(BaseModel):
    username:str

class QuizSubmitModel(BaseModel):
    token: str
    quiz_id: int
    score: int

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