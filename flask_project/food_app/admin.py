from food_app import admin , db , ModelView
from .models import *

admin.add_view(ModelView(User,db.session))
admin.add_view(ModelView(Restaurant , db.session))
admin.add_view(ModelView(Dish , db.session))
admin.add_view(ModelView(Address , db.session))
admin.add_view(ModelView(Menu , db.session))

