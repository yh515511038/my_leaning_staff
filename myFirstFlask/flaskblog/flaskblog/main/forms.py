from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, validators
from wtforms.validators import Length, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=50)])
    email = EmailField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[Length(min=5, max=50)])
    confirm_password = PasswordField("Confirm Password", validators=[EqualTo("password")])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=50)])
    password = PasswordField("Password", validators=[Length(min=5, max=50)])
    submit = SubmitField('Submit')

