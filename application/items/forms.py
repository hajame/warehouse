from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from application import db
from flask_login import current_user
from application.auth.models import User

class ItemForm(FlaskForm):
    name = StringField("Name:", [validators.Length(min=2, max=64, message="Name must be between 2-64 characters.")])
    volume = IntegerField("Volume:", [validators.NumberRange(min=0, max=2147483647, message="Must be between 0-2147483647")])
    amount = IntegerField("Amount:", [validators.NumberRange(min=0, max=2147483647, message="Must be between 0-2147483647")])
    warehouse = StringField("Warehouse:", [validators.Length(min=2, max=64, message="Name must be between 2-64 characters.")])
 
    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    name = StringField("Name:", [validators.Length(min=2, max=64, message="Name must be between 2-64 characters.")])
    
    class Meta:
        csrf = False