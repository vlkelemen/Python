from flask import render_template, request, flash, redirect, url_for, session
from datetime import datetime
from app import app, db
from app.forms import Myform, RegistrationForm
from app.models import ContactInfo


@app.route('/')
def main():
    return render_template('home.html', page=1)


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)




@app.route('/about')
def about():
    hobies = ("Programming", "Computer Games", "Board Games", "Tennis", "Basketball", "Reading", "Watching movies")
    return render_template('about.html', hobies=hobies, page=2)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Myform()
    if request.method == 'POST':
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
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    minute = now.strftime("%M")
    return render_template('contact.html', session=session, form=form, time=current_time, minute=minute, page=3)
    


@app.route('/contact_info', methods=['GET'])
def contact_info():
    contact_info_list = ContactInfo.query.all()
    return render_template('contact_info.html', contact_info_list=contact_info_list)


@app.route('/delete_contact_info/<int:number>', methods=['GET'])
def delete_contact_info(number):
    try:
        db.session.delete(ContactInfo.query.get_or_404(number))
        db.session.commit()
    except:
        db.session.rollback()
        return '<h1>Cannot delete!</h1>'
    return '<h1>Successfully deleted!</h1>'
