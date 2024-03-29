from food_app import db , UserMixin , login_manager
from werkzeug.security import generate_password_hash , check_password_hash


from datetime import datetime

"""On migration don't forget to timestamp the state of the database
by running db stamp head"""

class Restaurant(db.Model):

    __searchable__=['description','name']


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    telephone_number = db.Column(db.String(10) , nullable=False)
    average_price=db.Column(db.Integer , nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable=True)
    address_id=db.Column(db.Integer , db.ForeignKey('address.id') , nullable=True)

    dishes = db.relationship('Dish', backref='resto', lazy=True)
    menus = db.relationship('Menu', backref='resto', lazy=True)
    photos= db.relationship('ImageItem', lazy=True)
    
    def __repr__(self):
        return f"<Restaurant('{self.name}', '{self.date_created}')>"


class Address(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    street_address = db.Column(db.String(100) , nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state_id = db.Column(db.Integer ,db.ForeignKey('state.id') , nullable=True )
    country_id = db.Column(db.Integer ,db.ForeignKey('country.id') , nullable=True )
    
    resto = db.relationship('Restaurant', backref='address' , lazy=True)

    def __repr__(self):
        return f"<Address('{self.street_address}')>'"

class State(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(50) , nullable=False)
    country_id = db.Column(db.Integer ,db.ForeignKey('country.id') , nullable=True )

    def __repr__(self):
        return f"<State('{self.name}')>'"

class Country(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    code=db.Column(db.Integer , nullable=True)

    #address = db.relationship('Restaurant', backref='country', lazy=True)

    def __repr__(self):
        return f"<Country('{self.name}')>'"

class Menu(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    image_file =  db.Column(db.String(100), nullable=False ,default='default.jpg')
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"<Menu('{self.name}')>"
    

class Dish(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    image_file = db.Column(db.String(100), nullable=False ,default='default.jpg')
    price = db.Column(db.Integer , nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"<Dish('{self.name}', '{self.price}')>"

class Speciality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
     
    def __repr__(self):
        return f"<Speciality('{self.name}')>"

class Resto_speciality(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    speciality_id = db.Column(db.Integer, db.ForeignKey('speciality.id'), nullable=False)

    def __repr__(self):
        return f"<Resto_speciality('{self.restaurant_id}')>"


class ImageItem(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    photo_path=db.Column(db.String(100) , unique=True , nullable=False)
    restaurant_pk = db.Column(db.Integer , db.ForeignKey('restaurant.id') , nullable=True)

    def __repr__(self):
        return f"<ImageItem('{self.photo_path}')>"
#Used to load the user 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    resto = db.relationship('Restaurant', backref='user' , lazy=True)
    roles = db.relationship('Role', secondary='user_role')

    def __repr__(self):
        return f"<User('{self.username}', '{self.email}', '{self.image_file}')>"

    def set_password(self, password):
        self.password=generate_password_hash(password)

    def is_password(self,password_candidate):
        return check_password_hash(self.password,password_candidate)

class Role(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(20) , unique=True , nullable=False)

class User_role(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

"""
class RestaurantOwner(User):
    restaurant_id = db.Column(db.Integer,db.ForeignKey('restaurant.id'), nullable=False)

    def __repr__(self):
        return f"<RestaurantOwner('{self.username}','{self.email}')>"
"""
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    comments = db.relationship('Comment', backref='review' , lazy=True)

    def __repr__(self):
        return f"<Review('{self.user_id}', '{self.date_posted}')>"

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    to = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)

    def __repr__(self):
        return f"<Comment('{self.user_id}', '{self.date_posted}')>"



class Availabilty(db.Model):
    """ each field contains a time range 
    from the opening of the restaurant to closing 
    """

    id= db.Column(db.Integer , primary_key=True)

    monday=db.Column(db.String(20))
    tuesday=db.Column(db.String(20))
    wednesday=db.Column(db.String(20))
    thursday=db.Column(db.String(20))
    friday=db.Column(db.String(20))
    saturday=db.Column(db.String(20))
    sunday=db.Column(db.String(20))