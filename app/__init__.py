from flask import Flask

import uuid

import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    secret_key = os.getenv('FLASK_SECRET_KEY')

    if not secret_key:
        secret_key = uuid.uuid4().hex
        
    app.config['SECRET_KEY'] = secret_key

    from .routes import main

    from .auth.routes import auth
    from .api.routes import api
    
    app.register_blueprint(main)

    app.register_blueprint(auth, url_prefix = '/auth')
    app.register_blueprint(api, url_prefix = '/api')

    return app
