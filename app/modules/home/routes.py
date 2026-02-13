# app/modules/home/routes.py

from flask import render_template
from . import home_bp

# /
@home_bp.route('/')
def index():
    # render home/index.html
    return render_template('home/index.html')