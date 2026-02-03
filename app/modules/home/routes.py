from flask import render_template
from . import home_bp

# /
@home_bp.route('/')
def index():
    # show file index.html milik modul home
    return render_template('home/index.html')