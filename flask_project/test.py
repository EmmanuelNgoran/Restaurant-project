from food_app import db
from food_app.models import *

user_1 =User(username="Kingo" , email="emmm@gmail.com")
user_1.set_password("mypassword")
db.session.add(user_1)
db.session.commit()
##Add user role
##db > role -->