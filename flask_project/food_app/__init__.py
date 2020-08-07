from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import food_app.routes