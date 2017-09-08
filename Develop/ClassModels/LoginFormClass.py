from flask_wtf import Form, validators
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length


class LoginFormManager(Form):
    username = StringField('username', [DataRequired(), Length(min=4, max=25)])
    password = PasswordField([DataRequired(), Length(min=4, max=25)])
