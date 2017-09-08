from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired, length


class AddItemsManager(Form):
    name = StringField('name', [DataRequired(), length(min=4, max=25)])
    price = StringField('price', [DataRequired(), length(min=4, max=25)])
    quantity = StringField('quantity', [DataRequired(), length(min=4, max=25)])
