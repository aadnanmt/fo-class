# app/modules/gallery/__init__.py

from flask import Blueprint

# create bluprint galerry
gallery_bp = Blueprint('gallery', __name__, template_folder='templates')

# Import routes
from . import routes