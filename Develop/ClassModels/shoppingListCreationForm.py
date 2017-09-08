from flask_wtf import Form, validators, FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CreateShoppingList(FlaskForm):
    name = StringField('name', [DataRequired(), Length(min=4, max=25)])
    description = StringField('Description', [DataRequired(), Length(min=10, max=35)])