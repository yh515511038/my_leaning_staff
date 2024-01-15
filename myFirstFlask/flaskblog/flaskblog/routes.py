from flask import render_template, redirect, url_for, flash
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User


@app.route('/')
def home():
  return render_template('home.html', title='Home')


@app.route('register')
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    username = form.username.data
    email = form.email.data
    password = form.password.data
    flash('Register successfully!', 'success')
    return redirect(url_for('login'))
  else:
    flash('Username already exist, please choose another.', 'danger')
