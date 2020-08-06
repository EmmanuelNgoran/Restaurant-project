from food_app import app
from .models import *
from flask import render_template
from .forms import SearchForm

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
       print(f"{form.city_string.data}!")
        #return redirect(url_for('home'))
    return render_template('index.html', title='Home' , form=form)

@app.route('/result')
def result():
    return render_template('result.html')
