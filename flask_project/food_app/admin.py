from flask import Flask, url_for, redirect, render_template, request
from food_app import db ,login_manager , current_user,login_user,app,ModelView
from flask_admin import Admin , helpers , expose , AdminIndexView , form
from .models import *
from .forms import UserLoginForm , UserRegistrationForm
import os.path as op
from jinja2 import Markup
 

import flask_login as login

#admin.add_view(ModelView(User,db.session))


#from wtforms import form, fields, validators

file_path = op.join(op.dirname(__file__), 'static/images')
# Initialize flask-login
"""
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
"""

# Create customized model view class
class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated


class ImageView(MyModelView):
    """
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''
        print("%s" % (file_path,form.thumbgen_filename(model.photo_path)))
        return Markup('<img src="%s">' % (op.join(file_path))
                                                 )

    column_formatters = {
        'path': _list_thumbnail
    }
"""
    form_extra_fields = {
        'photo_path': form.ImageUploadField('ImageItem',
                                      base_path=file_path,
                                      thumbnail_size=(100, 100, True))
    }
# Create customized index view class that handles login & registration
class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = UserLoginForm()
        if form.validate_on_submit():
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = UserRegistrationForm()
        if form.validate_on_submit():
            user=User(username=form.username.data,email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))



# Initialize flask-login

# Create admin
admin = Admin(app, 'Restaurant Admin', index_view=MyAdminIndexView(), base_template='my_master.html')

# Add view
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Restaurant , db.session))
admin.add_view(MyModelView(Dish , db.session))
admin.add_view(MyModelView(Address , db.session))
admin.add_view(MyModelView(Menu , db.session))
admin.add_view(ImageView(ImageItem,db.session))



