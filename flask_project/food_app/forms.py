from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField , TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo 


class SearchForm(FlaskForm):
    cuisine_string = StringField('cuisine',
                           validators=[DataRequired(), Length(min=2, max=20)])

    city_string = StringField('city',
                           validators=[DataRequired(), Length(min=2, max=20)])
                           
    submit = SubmitField('Search')


class RestaurantCreationForm(FlaskForm):
    
    description = TextAreaField('Description',
                           validators=[DataRequired(), Length(min=2, max=200)])
    street_address = StringField('Your address',
                           validators=[DataRequired(), Length(min=2, max=20)])
    city = StringField('City',
                           validators=[DataRequired(), Length(min=2, max=20)])
    state = StringField('State',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired()])
    average_price = StringField('Average Price',
                        validators=[DataRequired()])
    specialities = StringField('Specialities',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone_number = StringField("Phone number" , validators=[DataRequired() , Length(min=8 , max=10)])
    
    
    submit = SubmitField('SAVE')

class UserRegistrationForm(FlaskForm):
    
    username = StringField("username" , validators=[DataRequired(), Length(min=2, max=200)])
    email = StringField("email" , validators=[DataRequired(), Length(min=2, max=200)])
    password = StringField("password" , validators=[DataRequired(), Length(min=2, max=200)])
    confirm_password = StringField("confirm password" , validators=[DataRequired(), Length(min=2, max=200)])

    submit = SubmitField('Sign Up')

class UserLoginForm(FlaskForm):
    email = StringField("email" , validators=[DataRequired(), Length(min=2, max=200)])
    password = StringField("password" , validators=[DataRequired(), Length(min=2, max=200)])
