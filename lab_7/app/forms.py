import phonenumbers
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp

from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           [DataRequired("Please enter your name."),
                            Length(min=4, max=10, message='Це поле має бути довжиною між 4 та 10 символів'),
                            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                   "Username should contain only letters, numbers, dots and underscores")])
    email = StringField('Email',
                        validators=[DataRequired("Please enter your email."), Email("Please enter corect email")])
    password = PasswordField('Password', validators=[Length(min=6), DataRequired("Enter password")])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired("Enter password"), EqualTo('password')])
    submit = SubmitField("Sign up")


    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")


class Myform(FlaskForm):
    name = StringField("Name",
                       [DataRequired("Please enter your name."),
                        Length(min=4, max=10, message='Це поле має бути довжиною між 4 та 10 символів')
                        ]
                       )
    email = StringField('Email',
                        validators=[DataRequired("Please enter your email."), Email("Please enter corect email")])
    phone = StringField('Phone', )
    subject = SelectField('Subject', choices=[('cpp', 'C++'), ('py', 'Python')])
    message = StringField('Message', validators=[DataRequired(),
                                                 Length(max=500, message='Це поле має бути довжиною до 500 символів')])

    def validate_phone(form, field):
        if len(field.data) > 13:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phonenumbers.parse(field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phonenumbers.parse("+38" + field.data)
            if not (phonenumbers.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')

    submit = SubmitField("Send")
