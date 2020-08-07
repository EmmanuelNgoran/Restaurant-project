from food_app import db

from datetime import datetime


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    address = db.Column(db.String(100) , nullable=True)
    city = db.Column(db.String(35) , nullable=False)
    country = db.Column(db.String(35) , nullable=False)
    telephone_number = db.Column(db.String(10) , nullable=False)
    average_price=db.Column(db.Integer , nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable=True)
    
    dishes = db.relationship('Dish', backref='resto', lazy=True)
    menus = db.relationship('Menu', backref='resto', lazy=True)
    user = db.relationship('User', backref='resto' , lazy=True)
    address = db.relationship('User', backref='resto' , lazy=True)

    def __repr__(self):
        return f"Restaurant('{self.name}', '{self.city}')"


class Address(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    street_address = db.Column(db.String(100) , nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state_id = db.Column(db.Integer ,db.ForeignKey('state.id') , nullable=True )
    country_id = db.Column(db.Integer ,db.ForeignKey('country.id') , nullable=True )

    def __repr__(self):
        return f"<Address('{self.street_address}')>'"

class State(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50) , nullable=False)
    country_id = db.Column(db.Integer ,db.ForeignKey('country.id') , nullable=True )

class Country(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    code=db.Column(db.Integer , nullable=True)

    address = db.relationship('Restaurant', backref='country', lazy=True)
class Menu(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    image_file =  db.Column(db.String(100), nullable=False ,default='default.jpg')
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"Menu('{self.name}')"
    

class Dish(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    image_file = db.Column(db.String(100), nullable=False ,default='default.jpg')
    price = db.Column(db.Integer , nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"Restaurant('{self.name}', '{self.price}')"

class Speciality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
     
    def __repr__(self):
        return f"Speciality('{self.name}')"

class Resto_speciality(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    speciality_id = db.Column(db.Integer, db.ForeignKey('speciality.id'), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class RestaurantOwner(User):
    restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"RestaurantOwner('{self.username}','{self.email}')"

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    def __repr__(self):
        return f"Review('{self.user_id}', '{self.date_posted}')"