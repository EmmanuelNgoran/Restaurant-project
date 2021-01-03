from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager , UserMixin , current_user, login_user
from flask_msearch import Search
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
search = Search()
db = SQLAlchemy(app)

login_manager=LoginManager(app)
#admin = Admin(app, 'Example: Auth', index_view=MyAdminIndexView(), base_template='my_master.html')
search.init_app(app)



# models.py


# views.py


import food_app.routes
import food_app.admin