from .food_app.models import User

"""test adding role to different user"""
try:
    user_1=models.User(username="Salomon Ali", email="salomonali@gmail.com")
    user_1.set_password("mypassword")
    user_1.roles.append(models.Role("Admin"))
    db.session.add(user_1)
    db.session.commit()

except Exception as e:
    print(e)
else:
    print("User has been inserted")