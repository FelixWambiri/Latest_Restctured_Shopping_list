from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, validators
from wtforms.validators import Email


class RegistrationForm(FlaskForm):
    firstname = StringField('firstname')
    lastname = StringField('Lastname')
    email = StringField('email', validators=[Email(message="Email Required")])
    username = StringField(' username')
    password = PasswordField('Password', [validators.DataRequired(),
                                          validators.EqualTo('confirm', message='Your password must match')])
    confirm = PasswordField('Confirm Password')
    # accept_tos = BooleanField('I accept the terms and conditions', [validators.DataRequired()])
