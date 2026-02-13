# app/__init__.py

from flask import Flask
from .config import Config

def create_app(config_class=Config):
    
    # create object flask
    app = Flask(__name__)
    
    # insert configuration (from file config.py)
    app.config.from_object(config_class)

    # Module Home (pth: app/modules/home/)
    from app.modules.home import home_bp
    app.register_blueprint(home_bp) # default url prefix ("/")

    # Module messages (path: app/modules/messages/)
    from app.modules.messages import messages_bp
    app.register_blueprint(messages_bp, url_prefix='/messages')

    # module gallery (path: app/modules/gallery/)
    from app.modules.gallery import gallery_bp
    app.register_blueprint(gallery_bp, url_prefix='/gallery')

    return app