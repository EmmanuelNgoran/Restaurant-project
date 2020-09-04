from functools import wraps
from food_app import app , db
from food_app.models import *
from flask import render_template , redirect , url_for , flash
from .forms import SearchForm , RestaurantCreationForm , UserRegistrationForm , UserLoginForm
from flask_login import current_user , login_user
from food_app.utils import login_required
#decorator for authentification


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
       print(f"{form.city_string.data}!")
        #return redirect(url_for('home'))
    return render_template('index.html', title='Home' , form=form)

@login_required
@app.route('/resto/create',methods=['GET', 'POST'])
def create_restaurant():
    form = RestaurantCreationForm()
    return render_template('create_restaurant.html', title='Create Restaurant' , form=form)

@login_required
@app.route('/resto/update',methods=['GET', 'POST'])
def restaurant_view():
    form = RestaurantCreationForm()
    is_valid =form.validate_on_submit()
    #errors=[ (f.label,f.errors) for f in form]
    print(f"is valid {is_valid}")
    if is_valid:
        app.logger.info("Success on creating restaurant")
    return render_template('restaurant.html', title='Home' , form=form)

@app.route('/result')
def result():
    return render_template('result.html')


@app.route('/login' , methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('home'))
    form =UserLoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and user.is_password(form.password.data):
            login_user(user)
            app.logger.info('successfully to log in')
            redirect(url_for('home'))
        else:
            flash('The details you have entered are not valid , please try again', 'danger')
            app.logger.info('failed to log in')
    return render_template('login.html' , form=form)


@app.route('/signup',methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
            return redirect(url_for('home'))
    form = UserRegistrationForm()
    #app.logger.info('Processing Sign up request')
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html' , form=form)

@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')