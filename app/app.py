from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///./site.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-please-change')

    
    db.init_app(app)


    migrate = Migrate(app, db)


    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    from . import auth
    app.register_blueprint(auth.bp)


    return app