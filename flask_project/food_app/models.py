from food_app import db

from datetime import datetime

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    address = db.Column(db.String(100) , nullable=True)
    city = db.Column(db.String(35) , nullable=False)
    telephone_number = db.Column(db.String(10) , nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    dishes = db.relationship('Dish', backref='resto', lazy=True)
    menus = db.relationship('Menu', backref='resto', lazy=True)

    def __repr__(self):
        return f"Restaurant('{self.name}', '{self.city}')"

class Menu(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    image_file = description = db.Column(db.String(100), nullable=False ,default='default.jpg')
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"Menu('{self.name}')"
    

class Dish(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    image_file = description = db.Column(db.String(100), nullable=False ,default='default.jpg')
    price = db.Column(db.Integer , nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"Restaurant('{self.name}', '{self.price}')"
