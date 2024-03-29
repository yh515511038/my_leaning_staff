from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email


class UpdateProfileForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  email = EmailField("Email", validators=[DataRequired()])
  image_file = FileField("Update Profile Image", validators=[FileAllowed(['jpg', 'png'])])
  submit = SubmitField("Update")
