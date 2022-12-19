from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Regexp


class Myform(FlaskForm):

    name = StringField("Name", validators=[DataRequired(),
                                           Length(min=4, max=10,
                                                  message='Length of this field must be between 4 and 10')])

    email = StringField("Email", validators=[DataRequired(), Email(message='Enter correct email')])

    phone = StringField("Phone", validators=[DataRequired(),
                                             Regexp(regex='^\+380[0-9]{9}', message='Enter correct phone number')])

    library = SelectField("Library", choices=['Numpy', 'Pandas', 'Matplotlib', 'Seaborn'])

    message = TextAreaField("Message", validators=[DataRequired(), Length(max=500,
                                                                          message='Max length of this field is 500')])
    submit = SubmitField("Send")
