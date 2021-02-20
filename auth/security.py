from werkzeug.security import safe_str_cmp
from models.user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    # If username and password matches then return User otherwise None
    if user and safe_str_cmp(user.password, password):
        return user
    else:
        return None

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)