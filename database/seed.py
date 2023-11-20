
from pymongo import MongoClient

client = MongoClient("localhost:27017")
client.drop_database('pixel')
db = client.pixel

user = [
    {'first_name': 'Rick', 'last_name': 'Sanchez', 'username': 'rickSanches', 'gender': 'Male', 'date_of_birth': '1958-05-16', 'email': 'rick@example.com', 'password': 'WubbaLubbaDubDub'},
    {'first_name': 'Morty', 'last_name': 'Smith', 'username': 'mortysmith', 'gender': 'Male', 'date_of_birth': '2002-03-12', 'email': 'morty@example.com', 'password': 'ohgeez'},
    {'first_name': 'Walter', 'last_name': 'White', 'username': 'Walterwhite', 'gender': 'Male', 'date_of_birth': '1965-07-30', 'email': 'walter@example.com', 'password': 'Heisenberg'},
    {'first_name': 'Jesse', 'last_name': 'Pinkman', 'username': 'jessepinkguy', 'gender': 'Male', 'date_of_birth': '1984-01-21', 'email': 'jesse@example.com', 'password': 'yobitch'},
    {'first_name': 'Gus', 'last_name': 'Fring', 'username': 'gustavothefrang', 'gender': 'Male', 'date_of_birth': '1956-11-23', 'email': 'gus@example.com', 'password': 'LosPollosHermanos'},
    {'first_name': 'Skyler', 'last_name': 'White', 'username': 'skylerwhiteYO', 'gender': 'Female', 'date_of_birth': '1970-09-18', 'email': 'skyler@example.com', 'password': 'MoneyLaundering'},
    {'first_name': 'Hank', 'last_name': 'Schrader', 'username': 'kindasuslately', 'gender': 'Male', 'date_of_birth': '1969-03-15', 'email': 'hank@example.com', 'password': 'Minerals'},
    {'first_name': 'Hector', 'last_name': 'Salamanca', 'username': 'lookatmehector', 'gender': 'Male', 'date_of_birth': '1940-02-21', 'email': 'hector@example.com', 'password': 'DingDing'},
    {'first_name': 'Peter', 'last_name': 'Griffin', 'username': 'eypeeta', 'gender': 'Male', 'date_of_birth': '1970-06-06', 'email': 'peter@example.com', 'password': 'FreakinSweet'},
    {'first_name': 'Lois', 'last_name': 'Griffin', 'username': 'yeslois', 'gender': 'Female', 'date_of_birth': '1974-12-22', 'email': 'lois@example.com', 'password': 'FamilyGuy123'},
    {'first_name': 'Stewie', 'last_name': 'Griffin', 'username': 'stewie2k', 'gender': 'Male', 'date_of_birth': '2001-04-03', 'email': 'stewie@example.com', 'password': 'VictoryIsMine'},
    {'first_name': 'Brian', 'last_name': 'Griffin', 'username': 'briandogystyle', 'gender': 'Male', 'date_of_birth': '1996-08-08', 'email': 'brian@example.com', 'password': 'GentlemanAndScholar'},
    {'first_name': 'Meg', 'last_name': 'Griffin', 'username': 'megladon', 'gender': 'Female', 'date_of_birth': '1995-01-13', 'email': 'meg@example.com', 'password': 'Megatron'},
    {'first_name': 'Glenn', 'last_name': 'Quagmire', 'username': 'gigidi', 'gender': 'Male', 'date_of_birth': '1959-12-08', 'email': 'quagmire@example.com', 'password': 'Giggity'},
    {'first_name': 'Saul', 'last_name': 'Goodman', 'username': 'slippingjimmy', 'gender': 'Male', 'date_of_birth': '1964-02-26', 'email': 'saul@example.com', 'password': 'BetterCallSaul'}
]
patient = [
    {"user_id": 1, "addiction_score": 32, "depression_score": 20, "adhd_score": 80, "insomnia_score": 21},
    {"user_id": 2, "addiction_score": 21, "depression_score": 15, "adhd_score": 70, "insomnia_score": 18},
    {"user_id": 3, "addiction_score": 45, "depression_score": 25, "adhd_score": 100, "insomnia_score": 43},
    {"user_id": 4, "addiction_score": 52, "depression_score": 35, "adhd_score": 150, "insomnia_score": 55},
    {"user_id": 5, "addiction_score": 11, "depression_score": 10, "adhd_score": 40, "insomnia_score": 39}
]
doctor = [
    {"user_id": 6, "specialty": "Cardiologist", "schedualed_sessions": 10, "years_of_exp": 15},
    {"user_id": 7, "specialty": "Pediatrician", "schedualed_sessions": 8, "years_of_exp": 20},
    {"user_id": 8, "specialty": "Dermatologist", "schedualed_sessions": 12, "years_of_exp": 10},
    {"user_id": 9, "specialty": "Psychiatrist", "schedualed_sessions": 6, "years_of_exp": 18},
    {"user_id": 10, "specialty": "Orthopedic Surgeon", "schedualed_sessions": 15, "years_of_exp": 25}
]
admin = [
    {"user_id": 11, "admin_role": "Superadmin", "permissions": 15},
    {"user_id": 12, "admin_role": "Administrator", "permissions": 7},
    {"user_id": 13, "admin_role": "Moderator", "permissions": 3}
]
quiz = [
    {"patient_id": 1, "quiz_date": "2023-11-01", "quiz_score": 75},
    {"patient_id": 2, "quiz_date": "2023-11-02", "quiz_score": 92},
    {"patient_id": 3, "quiz_date": "2023-11-03", "quiz_score": 60},
    {"patient_id": 4, "quiz_date": "2023-11-04", "quiz_score": 85},
    {"patient_id": 5, "quiz_date": "2023-11-05", "quiz_score": 78}
]

message = [
    {"sender_id": 1, "receiver_id": 2, "content": "Hello, how are you?", "message_date": "2023-11-06 09:30:00"},
    {"sender_id": 2, "receiver_id": 1, "content": "I'm doing well, thanks!", "message_date": "2023-11-06 09:35:00"},
    {"sender_id": 3, "receiver_id": 1, "content": "Can you help me with a task?", "message_date": "2023-11-06 10:15:00"},
    {"sender_id": 1, "receiver_id": 3, "content": "Sure, what do you need?", "message_date": "2023-11-06 10:20:00"},
    {"sender_id": 4, "receiver_id": 2, "content": "Meeting tomorrow at 3 PM.", "message_date": "2023-11-06 12:45:00"}
]
alert = [
    {"patient_id": 1, "alert_date": "2023-11-06 08:15:00", "alert_type": "Critical"},
    {"patient_id": 2, "alert_date": "2023-11-06 10:30:00", "alert_type": "High"},
    {"patient_id": 3, "alert_date": "2023-11-06 12:45:00", "alert_type": "Medium"},
    {"patient_id": 4, "alert_date": "2023-11-06 14:20:00", "alert_type": "Low"},
    {"patient_id": 5, "alert_date": "2023-11-06 16:55:00", "alert_type": "Critical"}
]

usage_stats = [
    {"user_id": 1, "stats_date": "2023-01-10"},
    {"user_id": 2, "stats_date": "2023-01-12"},
    {"user_id": 3, "stats_date": "2023-01-15"},
    {"user_id": 4, "stats_date": "2023-01-20"},
    {"user_id": 5, "stats_date": "2023-01-25"}
]

db.user.insert_many(user)
db.patient.insert_many(patient)
db.doctor.insert_many(doctor)
db.admin.insert_many(admin)
db.quiz.insert_many(quiz)
db.message.insert_many(message)
db.alert.insert_many(alert)
db.usage_stats.insert_many(usage_stats)