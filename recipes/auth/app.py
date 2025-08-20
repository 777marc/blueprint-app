import functools

from flask_login import login_user, logout_user, current_user, login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from recipes.auth.models import User
from recipes.app import bcrypt

bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            print(f"User {user.username} logged in")
            return redirect(url_for('index'))
        
    return render_template('login.html')


@bp.route('/register')
def register():
    return render_template('auth/register.html')