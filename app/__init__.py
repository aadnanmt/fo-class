from flask import Flask
from .config import Config

def create_app(config_class=Config):
    # create object flask
    app = Flask(__name__)
    
    # insert configuration (from file config.py)
    app.config.from_object(config_class)

    # Modul Home (pth: app/modules/home/__init__.py)
    from app.modules.home import home_bp
    
    # url_prefix='/'
    app.register_blueprint(home_bp)
    
    return app