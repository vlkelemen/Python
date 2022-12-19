from flask import render_template, request, flash, redirect, url_for, session
import datetime
from loguru import logger

from app import app
from app.forms import ContactForm


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Home')


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        logger.add("out.log")
        logger.debug(f"The form is sended in {datetime.datetime.now()}")
        logger.debug(f"Name = {form.name.data}")
        logger.debug(f"Email = {form.email.data}")
        logger.debug(f"Phone = {form.phone.data}")
        logger.debug(f"Subject = {form.subject.data}")
        logger.debug(f"Message = {form.message.data}")
        session['name'] = form.name.data
        session['email'] = form.email.data
        flash(f"Дані надіслано успішно: {form.name.data}, {form.email.data}", category='success')
        return redirect(url_for("contact"))

    elif request.method == 'POST':
        flash("Валідація з Post не пройшла", category='warning')

    form.name.data = session.get("name")
    form.email.data = session.get("email")
    return render_template('contact.html', form=form)


@app.route('/reset', methods=["GET", "POST"])
def reset():
    if session.get('email') is not None and session.get('name') is not None:
        session.pop("email")
        session.pop("name")
        return redirect(url_for("contact"))
    return redirect(url_for("contact"))
