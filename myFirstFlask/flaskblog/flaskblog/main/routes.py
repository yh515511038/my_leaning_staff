from flask import render_template, redirect, url_for, flash, Blueprint
from flaskblog import db
from flaskblog.main.forms import RegistrationForm, LoginForm
from flaskblog.main.models import User


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
  return render_template('home.html', title='Home')


@main.route('/register')
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    username = form.username.data
    email = form.email.data
    password = form.password.data
    user = User.query.filter_by(username=username).first()
    if not user:
      db.session.add(user)
      db.session.commit()
      flash('Register successfully!', 'success')
      return redirect(url_for('main.login'))
    else:
      flash('Username already exist, please choose another.', 'danger')
  else:
    return render_template('register.html', form=form, title='Sign Up')


@main.route('/login')
def login():
  form = LoginForm()
  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data
    user = User.query.filter_by(username=username).first()
    if user and password == user.password:
      flash(f'Welcome back, {user.username}!', 'success')
      return redirect(url_for('main.home'))
    else:
      flash('Username or password is incorrect, please check.', 'danger')
  else:
    return render_template('login.html', form=form, title='Sign In')