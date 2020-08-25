import os
from flask import Flask
from dotenv import load_dotenv


def create_app():

    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path)

    app = Flask(__name__, template_folder='templates')

    app.config['CSRF_SESSION_KEY'] = os.environ.get('CSRF_SESSION_KEY')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

    from app.controllers import app as app_module
    app.register_blueprint(app_module)

    return app
