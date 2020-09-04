from flask_project.food_app import db
from flask_project.food_app.models import User

##insert a user in the database and test the add method

print("*"*5+"All users"+"*"*5)
print(User.query.all())
#add a user to the user table
try:
    user_1=User(username="EmmanuelNgoran", email="emmangoran@gmail.com")
    user_1.set_password("mypassword")
    db.session.add(user_1)
    db.session.commit()
except Exception as e:
    print(e)
else:
    print("User has been inserted")