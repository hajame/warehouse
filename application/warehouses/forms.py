from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class WarehouseForm(FlaskForm):
    name = StringField("Name:", [validators.Length(min=2, max=128, message="Must be within 2-128 characters.")])
    volume = IntegerField("Volume:", [validators.NumberRange(min=0, max=2147483647, message="Must be between 0-2147483647")])
 
    class Meta:
        csrf = False