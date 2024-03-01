from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Length, EqualTo, Email, ValidationError
from flaskblog.users.models import User


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=50)])
    email = EmailField("Email", validators=[Email()])
    password = PasswordField("Password", validators=[Length(min=5, max=50)])
    confirm_password = PasswordField("Confirm Password", validators=[EqualTo("password")])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exists!")
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exists!")
         


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[Length(min=2, max=50)])
    password = PasswordField("Password", validators=[Length(min=5, max=50)])
    remember = BooleanField(default=False)
    submit = SubmitField('Submit')

