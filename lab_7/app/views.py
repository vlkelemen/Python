from flask import render_template, request, flash, redirect, url_for, session
from datetime import datetime
from app import app, db, bcrypt
from app.forms import Myform, RegistrationForm, LoginForm
from app.models import ContactInfo, User


@app.route('/')
def main():
    return render_template('home.html', page=1)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        flash(f'Account created for {form.username.data} !', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = bcrypt.generate_password_hash(form.password.data)
        remember = form.remember.data

        if User.query.filter_by(email=email, password=password):
            flash(f'Logged in as {form.email.data} !', category='success')
        else:
            flash(f'Not correct data passed!', category='danger')
        return redirect(url_for("main"))
    return render_template('login.html', form=form)


@app.route('/users')
def users():
    all_users = User.query.all()
    return render_template('users.html', all_users=all_users)


@app.route('/about')
def about():
    hobies = ("Programming", "Computer Games", "Board Games", "Tennis", "Basketball", "Reading", "Watching movies")
    return render_template('about.html', hobies=hobies, page=2)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Myform()
    if request.method == 'GET':
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        minute = now.strftime("%M")
        return render_template('contact.html', session=session, form=form, time=current_time, minute=minute, page=3)

    if form.validate_on_submit():
        username = form.name.data
        email = form.email.data
        phone = form.phone.data
        subject = form.subject.data
        message = form.message.data
        session['name'] = username
        session['email'] = email

        contact_info = ContactInfo(username=username, email=email, phone=phone, subject=subject, message=message)
        db.session.add(contact_info)
        db.session.commit()

        form.name.data = 'виконався метод post і валідація успішно'
        flash(f"Дані успішно відправлено: {username} {email}", category='success')
        return redirect(url_for("contact"))

    flash("Не пройшла валідація з Post", category='warning')
    return redirect(url_for("contact"))


@app.route('/contact_info', methods=['GET'])
def contact_info():
    user_contact_id = request.args.get('id')
    if user_contact_id:
        contact_info_list = ContactInfo.query.filter_by(id=user_contact_id)
    else:
        contact_info_list = ContactInfo.query.all()
    return render_template('contact_info.html', contact_info_list=contact_info_list)


@app.route('/delete_session')
def delete_email():
    session.pop('email', default=None)
    session.pop('name', default=None)
    return '<h1>Session deleted!</h1>'
