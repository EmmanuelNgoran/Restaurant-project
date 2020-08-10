from food_app import app
from .models import *
from flask import render_template
from .forms import SearchForm , RestaurantCreationForm


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
       print(f"{form.city_string.data}!")
        #return redirect(url_for('home'))
    return render_template('index.html', title='Home' , form=form)


@app.route('/resto',methods=['GET', 'POST'])
def restaurant():
    form = RestaurantCreationForm()
    app.logger.info('Processing default request')
    if form.validate_on_submit():
        app.logger.info(f"form fields : description :  {form.description.data}\nemail: \t{form.email.data}")
    return render_template('restaurant.html', title='Home' , form=form)

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')