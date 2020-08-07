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
    address = StringField('Your address',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired()])
    specialities = StringField('Specialities',
                           validators=[DataRequired(), Length(min=2, max=20)])
    phone_number = StringField("Phone number" , validators=[DataRequired() , Length(min=8 , max=10)])
    
    
    submit = SubmitField('SAVE')
