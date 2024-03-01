from flask import Blueprint, render_template, flash, redirect, url_for, request
from flaskblog.main.forms import LoginForm


main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template("index.html")


@main.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if request.method == "POST"and form.validate_on_submit():
        print("POST method!")
        username = form.username.data
        password = form.password.data
        print(f"usrname: {username}, password: {password}")
        if username == 'admin' and password == 'qwe123':
            print("login success!")
            flash(f"Welcome back, {username.capitalize()}!", "success")
            redirect(url_for('main.home'))
        else:
            flash(f"Username or password is invalid, please check!", "warning")
    return render_template("login.html", form=form)
