
from pymongo import MongoClient

db = MongoClient("localhost:27017").pixel

db.drop_collection('admin')
db.user.delete_many({'perms':{'$gte':8}})
users = [
{  
  "username": "supa",
  "email": "supa@example.com",
  "hashed_password": "$2b$12$J.Nf2M5MWNIVS60mVMeq/uGLOndrowMNjQvSIKY3LTsTZPV8U8Mci",
  "gender": "female",
  "date_of_birth": "2005-03-25",
  "perms": 17
},
{  
  "username": "mod1",
  "email": "mod1@example.com",
  "hashed_password": "$2b$12$J.Nf2M5MWNIVS60mVMeq/uGLOndrowMNjQvSIKY3LTsTZPV8U8Mci",
  "gender": "male",
  "date_of_birth": "2005-03-25",
  "perms": 9
},
{  
  "username": "mod2",
  "email": "mod2@example.com",
  "hashed_password": "$2b$12$J.Nf2M5MWNIVS60mVMeq/uGLOndrowMNjQvSIKY3LTsTZPV8U8Mci",
  "gender": "male",
  "date_of_birth": "2005-03-25",
  "perms": 9
},
]

admins = [
    {"username": 'supa', "role": "superadmin"},
    {"username": 'mod1', "role": "moderator"},
    {"username": 'mod2', "role": "moderator"}
]

db.user.insert_many(users)
db.admin.insert_many(admins)
print("Database Seeded")