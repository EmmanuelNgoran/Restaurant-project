from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField , TextAreaField , PasswordField , SelectField
from wtforms.validators import DataRequired, Length, EqualTo ,Email, ValidationError
from food_app.models import User
from food_app import db
from food_app.utils import CITY,COUNTRY

class SearchForm(FlaskForm):
    cuisine_string = StringField('cuisine',
                           validators=[DataRequired(), Length(min=2, max=20)])

    city_string = StringField('city',
                           validators=[DataRequired(), Length(min=2, max=20)])
                           
    submit = SubmitField('Search')


class RestaurantCreationForm(FlaskForm):

    name=StringField("Name" , validators=[DataRequired(), Length(min=4 , max=35)])
    
    description = TextAreaField('Description',
                           validators=[DataRequired(), Length(min=2, max=200)])
    street_address = StringField('Your address',
                           validators=[DataRequired(), Length(min=2, max=50)])
    city = SelectField('City',
                           choices=CITY)
    """state = StringField('State',
                           validators=[DataRequired(), Length(min=2, max=20)])"""
    email = StringField('Email',
                        validators=[DataRequired() , Email()])
    average_price = StringField('Average Price',
                        validators=[DataRequired()])
    specialities = StringField('Specialities',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone_number = StringField("Phone number" , validators=[DataRequired() , Length(min=8 , max=10)])
    
    
    #submit = SubmitField('SAVE')

class UserRegistrationForm(FlaskForm):
    
    username = StringField("username" , validators=[DataRequired(), Length(min=2, max=200)])
    email = StringField("email" , validators=[DataRequired(), Length(min=2, max=200) , Email()])
    password = PasswordField("password" , validators=[DataRequired(), Length(min=2, max=200)])
    confirm_password = PasswordField("confirm password" , validators=[DataRequired(), Length(min=2, max=200)])

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
    
    #submit = SubmitField('Sign Up')

class UserLoginForm(FlaskForm):
    email = StringField("email" , validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField("password" , validators=[DataRequired(), Length(min=2, max=20)])

    def validate_email(self, email):
        user = self.get_user()
        if user is None:
            raise ValidationError('Invalid user')
        if not user.is_password(self.password.data):
            raise ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(email=self.email.data).first()