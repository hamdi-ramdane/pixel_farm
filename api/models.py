from pydantic import BaseModel , validator, EmailStr
from datetime import date,datetime
from re import match
from pymongo import MongoClient

db = MongoClient("localhost:27017").pixel

class User(BaseModel):
    username: str
    email: EmailStr 
    perms:int = 1

# Auth ===================================================================
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
    @validator("content")
    def check_content_size(cls,value):
        if len(value) > 1000:
            raise ValueError("Message Too Large")
        return value

class NotificationModel(BaseModel):
    receiver_username:str
    content:str

# Quiz ===================================================================
# ========================================================================

class QuizSubmitModel(BaseModel):
    depression_score:int = 0
    addiction_score:int = 0
    insomnia_score:int = 0
    adhd_score:int = 0
    @validator("depression_score","addiction_score","insomnia_score","adhd_score")
    def check_score_range(cls,value):
        if value < 0 or value > 100 :
            raise ValueError("Invalid Score.  ( 0 <= SCORE <= 100 )")
        return value
# Dashboard ==============================================================
# ========================================================================
class UpdateProfileModel(BaseModel):
    password: str = 'password123' 
    gender: str = "male"
    date_of_birth: date = date(2005,3,25)
    @validator("password")
    def check_length_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
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

class BanUserModel(BaseModel):
    username:str

class DeleteUserModel(BaseModel):
    username:str

class GrantAdminModel(BaseModel):
    username:str

