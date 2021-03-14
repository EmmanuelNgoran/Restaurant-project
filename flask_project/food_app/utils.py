from functools import wraps
from flask_login import current_user
from PIL import Image
import secrets
import os


CITY=[("QC","QUEBEC"),("MTL", "MONTREAL")]
COUNTRY=[("CA","CANADA")]

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

file_path = os.path.join(os.path.dirname(__file__), 'static\images')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if  not current_user.is_authenticated :
            print("Authenticated")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
        print("Authenticated")
    return decorated_function

def role_required(f,*args,**kwargs):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if  kwargs["user_role"] in [ role.name for role in current_user.role ] :
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_image(form_picture,restaurant_name):

    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(file_path, restaurant_name)
    if  not os.path.exists(picture_path):
        os.makedirs(picture_path)
    saved_file_dir= os.path.join(picture_path, picture_fn)
    print(saved_file_dir)
    i = Image.open(form_picture)
    #i.thumbnail(output_size)
    i.save(saved_file_dir)

    return picture_fn

