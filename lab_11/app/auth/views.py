import os 

from PIL import Image, ImageOps
import secrets
from flask import render_template, redirect, flash, url_for, request, current_app
from flask_login import login_required, logout_user, login_user, current_user

from app import db, bcrypt
from app.auth import auth_bp
from app.auth.forms import LoginForm, RegistrationForm, UpdateAccountForm, ChangePasswordForm
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
    return redirect(url_for('home.main'))

@auth_bp.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', all_users=all_users)


@auth_bp.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if request.method == "GET":
        pass_form = ChangePasswordForm()
        image_file = url_for('static', filename="images/" + current_user.image )
        return render_template('account.html', image_file=image_file, form=form, pass_form=pass_form)
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        image = form.image.data
        about_me = form.about_me.data

        current_user.username = username
        current_user.email = email
        current_user.image = save_picture(image)
        current_user.about_me = about_me

        print(image)
        db.session.add(current_user)
        db.session.commit()

        flash(f"Account info successfully updated", category='success')
        return redirect(url_for("auth.account"))
    flash(f"Not correct data passed", category='warning')
    return redirect(url_for("auth.account"))

def save_picture(from_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(from_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/images', picture_fn)
    from_picture.save(picture_path)

    output_size = (125, 125)
    image = Image.open(from_picture)
    thumb = ImageOps.fit(image, output_size, Image.ANTIALIAS)
    thumb.save(picture_path)
    
    return picture_fn


@auth_bp.route('/change_password', methods=['POST'])
@login_required
def change_pwd():
    pass_form = ChangePasswordForm()
    if pass_form.validate_on_submit():
        password = bcrypt.generate_password_hash(pass_form.new_password.data)
        current_user.password = password
        db.session.add(current_user)
        db.session.commit()

        flash(f"Account info successfully updated", category='success')
        return redirect(url_for("auth.account"))
    flash(f"Not correct data passed", category='warning')
    return redirect(url_for("auth.account"))
