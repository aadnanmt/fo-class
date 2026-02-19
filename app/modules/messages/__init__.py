# app/modules/messages/__init__.py

from flask import Blueprint

# blueprint messages
messages_bp = Blueprint('messages', __name__, template_folder='templates')

# import routes.py
from . import routes