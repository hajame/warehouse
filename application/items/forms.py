from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from application import db
from flask_login import current_user
from application.auth.models import User

class SearchForm(FlaskForm):
    name = StringField("Name:", [validators.Length(min=2, max=64, message="Name must be between 2-64 characters.")])
    
    class Meta:
        csrf = False

class ItemEditForm(SearchForm):
    volume = IntegerField("Volume:", [validators.NumberRange(min=0, max=2147483647, message="Must be between 0-2147483647")])
 
    class Meta:
        csrf = False

class ItemForm(ItemEditForm):
    warehouse = StringField("Warehouse:", [validators.Length(min=2, max=64, message="Name must be between 2-64 characters.")])
    amount = IntegerField("Amount:", [validators.NumberRange(min=0, max=2147483647, message="Must be between 0-2147483647")])
 
    class Meta:
        csrf = False

class AmountForm(FlaskForm):
    amount = IntegerField("Amount:", [validators.NumberRange(min=0, max=2147483647, message="Must be between 0-2147483647")])
 
    class Meta:
        csrf = False
