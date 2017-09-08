from flask_wtf import Form, validators
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length


class DeleteItemsManager(Form):
    name = StringField('name', [DataRequired(), Length(min=4, max=25)])

