from food_app import db , app
from food_app.models import *

"""
user_1 =User(username="Kingo" , email="emmm@gmail.com")
user_1.set_password("mypassword")
db.session.add(user_1)
db.session.commit()
##Add user role
##db > role -->
"""
"""

resto_1= Restaurant(name="Mc Boulet" , description="Welcto thejbj best burger",
telephone_number="12kk561" , average_price=150)
address_1=Address(street_address="palb omnare", city="Quebec")
resto_1.address=address_1
db.session.add(resto_1)
db.session.commit()
"""

"""test adding role to different user"""
"""
user_1=User(username="Salomon Ali", email="salomonali@gmail.com")
user_1.set_password("mypassword")
user_1.roles.append(Role(name="Admin"))
db.session.add(user_1)
db.session.commit()


print("User has been inserted")
"""
# m-search test
from flask_msearch import Search

search = Search()
search.init_app(app)

# models.py


# views.py
def w_search():
    results = Restaurant.query.msearch("M",fields=['name']).all()
   
    return results

print("result are :", w_search())
