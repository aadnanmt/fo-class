from flask import Blueprint

# create Blueprint
home_bp = Blueprint('home', __name__, template_folder='templates')
messages_bp = Blueprint('messages', __name__, template_folder ='templates')

# import module routes
from . import routes