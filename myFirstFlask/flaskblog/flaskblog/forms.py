from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
  username = StringField('Username', DataRequired(), Length(min=2, max=50))
  email = StringField('Email', DataRequired(), Length(min=2, max=100))
  password = PasswordField('Password', DataRequired(), Length(min=5, max=100))
  confirm_password = PasswordField('Confirm password', DataRequired(), EqualTo('password'))
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data)
    if user:
      return ValidationError('Username already exist, please choose another.')
    

class LoginForm(FlaskForm):
  username = StringField('Username', DataRequired(), Length(min=2, max=50))
  password = PasswordField('Password', DataRequired(), Length(min=2, max=5))
  submit = SubmitField('Sign In')
