from functools import wraps
from food_app import app , db
from food_app.models import *
from flask import (render_template , redirect , url_for , flash , request, jsonify , g)
from .forms import SearchForm , RestaurantCreationForm , UserRegistrationForm , UserLoginForm , RestaurantUpdateForm
from flask_login import current_user , login_user
from food_app.utils import login_required , save_image , allowed_file
from markupsafe import escape

import random
#decorator for authentification
decoy=["Burger King ", "Mc Donal","lacalebasse", "some rst","supoer"]

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

    if form.validate_on_submit():
        resto= Restaurant(name=form.name.data , description=form.description.data,
            telephone_number=form.phone_number.data , average_price=form.average_price.data)
        address=Address(street_address=form.street_address.data, city=form.city.data)
        resto.address=address
        db.session.add(resto)
        db.session.commit()
        app.logger.info('Restaurant successfully created')
        return redirect(url_for('home'))
    return render_template('create_restaurant.html', title='Create Restaurant' , form=form)

@login_required
@app.route('/resto/update/<int:resto_id>',methods=['GET', 'POST'])
def restaurant_view(resto_id):
    id=escape(resto_id)
    resto=Restaurant.query.filter_by(id=id).first()
    g.resto=resto
    form = RestaurantUpdateForm()
    if form.validate_on_submit():
        resto.name=form.name.data
        resto.description=form.description.data
        resto.address.street_address=form.street_address.data
        db.session.commit()
        return redirect(url_for('restaurant_view',resto_id=resto_id))
    if request.method == 'GET':
        # to be changed -Add a method to encapsulate the 
        #following lines
        id=resto.id
        form.name.data=resto.name
        form.description.data=resto.description
        form.street_address.data=resto.address.street_address
        form.phone_number.data =resto.telephone_number
        form.average_price.data=resto.average_price


    return render_template('update_restaurant.html', title='Home' ,id=id, form=form , resto=resto)

@app.route('/result')
def result():
    restaurants = Restaurant.query.all()
    return render_template('result.html' , restaurants=restaurants)


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

def w_search(content):
    results = Restaurant.query.msearch(content,fields=['name','description']).all()
    return results

"""Api call"""
@app.route('/api/search' , methods=['GET'])
def search_end_point():
    response=" "
    content = request.args.get('content', 0, type=str)
    city = request.args.get('city', 0, type=str)

    if len(content) > 0:
        res = w_search(content)
        response=[ {'name':ob.name,'id':ob.id}  for ob in res]    

    return jsonify(response)

@app.route('/api/add/cover', methods=['POST'])
def add_cover():
    if request.method == 'POST':
        app.logger.info(f"post method")
        # check if the post request has the file part
        print(request.files)
        if request.files:
            if 'files[]' in request.files.keys(): 
                for file_elem in request.files.getlist('files[]'):
                    print(f"-- {file_elem}")
                    if allowed_file(file_elem.filename):
                        image_name= save_image(file_elem,'Restaurant')
                        new_image = ImageItem(photo_path=image_name)
                        db.session.add(new_image)
                        db.session.commit()
                    app.logger.info(f"The file name is{file_elem.filename}")
            return "accepted"

        return "error"

    
@app.route('/api/add/menu', methods=['POST'])
def add_menu():
    if request.form.get('menu_name') and request.form.get('id'):
        if request.files['files']:
            
            pass
            
        

@app.route('/api/add/dish', methods=['POST'])
def add_dish():
    data_menu=request.form
    print(request)
    if data_menu.get('dish_name') and data_menu.get('dish_option'):
        app.logger.info(f"The dish is {data_menu.get('dish_name')} and its option are {data_menu.get('dish_option')}")
        if data_menu.get("dish_desc"):
            app.logger.info(f"The dish description is {data_menu.get('dish_desc')}")
        return "success"
    else:
        return "error"

@app.route('/about')
def about():
    return render_template('about.html')
