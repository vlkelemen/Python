from datetime import datetime

from flask import session, render_template, request, redirect, url_for, flash

from app import db
from app.feedback import feedback_bp
from app.feedback.forms import Myform
from app.feedback.models import ContactInfo


@feedback_bp.route('/contact', methods=['GET', 'POST'])
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


@feedback_bp.route('/contact_info', methods=['GET'])
def contact_info():
    user_contact_id = request.args.get('id')
    if user_contact_id:
        contact_info_list = ContactInfo.query.filter_by(id=user_contact_id)
    else:
        contact_info_list = ContactInfo.query.all()
    return render_template('contact_info.html', contact_info_list=contact_info_list)


@feedback_bp.route('/delete_session')
def delete_email():
    session.pop('email', default=None)
    session.pop('name', default=None)
    return '<h1>Session deleted!</h1>'
