from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager , UserMixin , current_user, login_user

import logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager=LoginManager(app)
#admin = Admin(app, 'Example: Auth', index_view=MyAdminIndexView(), base_template='my_master.html')


import food_app.routes
import food_app.admin