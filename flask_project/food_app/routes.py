from food_app import app
from .models import *
from flask import render_template
from .forms import SearchForm , RestaurantCreationForm , UserRegistrationForm , UserLoginForm


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

@app.route('/login' , methods=['GET', 'POST'])
def login():
    form =UserLoginForm()
    if form.validate_on_submit():
        app.logger.info(f"form fields : email: \t{form.email.data}")
    return render_template('login.html' , form=form)

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    form = UserRegistrationForm()
    #app.logger.info('Processing Sign up request')
    if form.validate_on_submit():
        app.logger.info(f"form fields : username :  {form.username.data}\nemail: \t{form.email.data}")
    return render_template('signup.html' , form=form)

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')