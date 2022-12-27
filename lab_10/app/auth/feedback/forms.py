import phonenumbers
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, ValidationError


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
