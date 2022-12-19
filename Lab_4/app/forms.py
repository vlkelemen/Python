from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import Email, DataRequired, Length, ValidationError, Regexp
from wtforms.widgets import TextArea


class ContactForm(FlaskForm):
    subjects = [('1', 'english'), ('2', 'math'), ('3', 'nature')]
    name = StringField("Name: ", validators=[DataRequired(), Length(min=4, max=10,
                                            message='Name length must be between %(min)d and %(max)dcharacters')])
    email = StringField("Email: ", validators=[DataRequired(), Email(message='Wrong Email')])
    phone = StringField('Phone', validators=[DataRequired(message='Wrong Phone'), Length(min=13, max=13),
                                             Regexp(regex='^\+380[0-9]{9}')])
    subject = SelectField("Subject: ", choices=subjects)
    message = StringField("Message: ", widget=TextArea(), validators=[Length(max=500)])
    submit = SubmitField("Send")
