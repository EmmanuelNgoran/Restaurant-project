from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class SearchForm(FlaskForm):
    cuisine_string = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    city_string = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
                           
    submit = SubmitField('Search')