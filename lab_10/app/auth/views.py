from flask import render_template, redirect, flash, url_for
from flask_login import login_required, logout_user, login_user, current_user

from app import db, bcrypt
from app.auth import auth_bp
from app.auth.forms import LoginForm, RegistrationForm
from app.auth.models import User


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.username.data} !', category='success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.main'))
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        remember = form.remember.data
        user = User.query.filter_by(email=email).first()
        if user and user.verify_password(form.password.data):
            login_user(user, remember=remember)
            flash(f'Logged in as {form.email.data} !', category='success')
        else:
            flash(f'Not correct data passed!', category='danger')
        return redirect(url_for("home.main"))
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect(url_for('main'))

@auth_bp.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', all_users=all_users)


@auth_bp.route('/account')
@login_required
def account():
    return render_template('account.html')
