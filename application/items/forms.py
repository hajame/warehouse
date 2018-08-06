from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class ItemForm(FlaskForm):
    name = StringField("Name:", [validators.Length(min=2)])
    volume = IntegerField("Volume:", [validators.NumberRange(min=0, message="Cannot be negative")])
    amount = IntegerField("Amount:", [validators.NumberRange(min=0, message="Cannot be negative")])
 
    class Meta:
        csrf = False