from functools import wraps
from flask_login import current_user

CITY=[("QC","QUEBEC"),("MTL", "MONTREAL")]
COUNTRY=[("CA","CANADA")]

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
import os.path as op
file_path = op.join(op.dirname(__file__), 'static/images')
print(file_path)