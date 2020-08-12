from food_app import db
from food_app.models import *
db.create_all()
user_1 =User(username="King" , email="emm@gmail.com" , password="Emufub4uf")

db.session.add(user_1)
db.session.commit()