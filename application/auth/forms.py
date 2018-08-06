from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class UserForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, message="Name must be at least 2 characters long")])
    username = StringField("Username", [validators.Length(min=2, message="Username must be at least 2 characters long")])
    password = PasswordField("Password", [validators.Length(min=2, message="Password must be at least 2 characters long")])

    class Meta:
        csrf = False