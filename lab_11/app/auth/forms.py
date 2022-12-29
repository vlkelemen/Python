from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp
from flask_wtf.file import FileField, FileAllowed
from app.auth.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField("Username",
                           [DataRequired("Please enter your name."),
                            Length(min=4, max=10, message='Це поле має бути довжиною між 4 та 10 символів'),
                            Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                   "Username should contain only letters, numbers, dots and underscores")])
    email = StringField('Email',
                        validators=[DataRequired("Please enter your email."), Email("Please enter corect email")])
    password = PasswordField('Password', validators=[Length(min=6), DataRequired("Enter password")])
    confirm_password = PasswordField('Confirm password',
                                     validators=[DataRequired("Enter password"), EqualTo('password')])
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


class UpdateAccountForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email', validators=[Email()])
    about_me = TextAreaField("About me", validators=[Length(max=120, message='Too long')])
    image = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Update")

    def validate_email(self, field):
        if field.data != current_user.email:
            if User.query.filter_by(email=field.data).first():
                raise ValidationError('Email already used!')

    def validate_username(self, field):
        if field.data != current_user.username:
            if User.query.filter_by(username=field.data).first():
                raise ValidationError('Username already used')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password')
    new_password = PasswordField('New password',
                             validators=[Length(min=6,
                                                message='Password must be longer then 6')])
    confirm_password = PasswordField('Confirm password',
                                     validators=[DataRequired(), EqualTo("new_password")])
    submit = SubmitField("Change password")

    def validate_old_password(self, old_password):
        if not current_user.verify_password(old_password.data):
            raise ValidationError('Password is not correct')
