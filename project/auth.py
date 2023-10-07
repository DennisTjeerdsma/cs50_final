from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # obtain information from register post request
        username = request.form['username']
        password = request.form['password']
        password_confirmation = request.form['password_confirmation']
        email = request.form['email']

        #Check if email exists in database
        check_email = User.query.filter_by(email=email).first()
        
        if check_email:
            flash('Email is already taken, please try again')
            return redirect(url_for('auth.register'))
        
        # check if username in database
        check_user = User.query.filter_by(email=email).first()
        if check_user:
            flash('Username is already taken, please try again')
            return redirect(url_for('auth.register'))
        
        # Check if password matches confirmation

        if password != password_confirmation:
            flash('Passwords do not match!')
            return redirect(url_for('auth.register'))

        # Insert new user in database
        new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    else:
        return render_template('register.html')

@auth.route('/logout')
def logout():
    return 'Logout'