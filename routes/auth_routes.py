from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

from models.user import User
from extensions import db

auth = Blueprint('auth', __name__)

# Register Route
@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Registration Successful!')
        return redirect(url_for('auth.login'))

    return render_template('register.html')


# Login Route
@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            return redirect(url_for('task_routes.dashboard'))

        else:
            flash('Invalid Email or Password')

    return render_template('login.html')


# Logout Route
@auth.route('/logout')
def logout():

    logout_user()

    return redirect(url_for('auth.login'))