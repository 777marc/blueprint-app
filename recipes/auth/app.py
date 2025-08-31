import functools

from flask_login import login_user, logout_user, current_user, login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)
from werkzeug.security import check_password_hash, generate_password_hash
from recipes.auth.models import User


bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and current_app.extensions['bcrypt'].check_password_hash(user.password, password):
            login_user(user)
            print(f"User {user.username} logged in")
            return redirect(url_for('index'))
        
    return render_template('auth/login.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = 'user'
        hashed_password = current_app.extensions['bcrypt'].generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password, role=role)
        current_app.extensions['db'].session.add(new_user)
        current_app.extensions['db'].session.commit()
        return redirect('/login')

    return render_template('auth/register.html')