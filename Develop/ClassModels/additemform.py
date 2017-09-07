from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class AddItemsManager(Form):
    name = StringField('name', [DataRequired(), Length(min=4, max=25)])
    price = StringField('price', [DataRequired(), Length(min=4, max=25)])
    quantity = StringField('quantity'[DataRequired(), Length(min=4, max=25)])
