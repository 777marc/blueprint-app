from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from .extensions import db, login_manager
from recipes.auth.models import User

import os

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///./site.db')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-please-change')

    db.init_app(app)
    login_manager.init_app(app)

    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))

    @app.route('/')
    def hello():
        return render_template('index.html')

    from recipes.auth.app import bp as auth_bp
    app.register_blueprint(auth_bp)


    return app