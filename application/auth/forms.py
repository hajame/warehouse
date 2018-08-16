from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class UserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=32, message="Name must be 2-32 characters long")])
    username = StringField("Username", [validators.Length(min=2, max=32, message="Username must be 2-32 characters long"), validators.Regexp('^\w+$', 0, 'Username must contain only letters, numbers or underscores')])
    password = PasswordField("Password", [validators.equal_to('confirm', message='Passwords must match'), validators.Length(min=4, max=32, message="Password must be at least 4 characters long"), validators.Regexp('^\w+$', 0, 'Passwords must contain only letters, numbers or underscores')])
    confirm  = PasswordField('Repeat Password')

    class Meta:
        csrf = False