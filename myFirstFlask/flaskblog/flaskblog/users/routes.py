from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from flaskblog import db
from flaskblog.users.forms import UpdateProfileForm
from flaskblog.users.utils import save_picture

users = Blueprint('users', __name__)


@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateProfileForm()
    if request.method == "POST" and form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        print(f"form.image_file.data: {form.image_file.data}")
        if form.image_file.data:
            image_filename = save_picture(form.image_file.data)
            current_user.image_file = image_filename
        db.session.commit()
        flash("Your profile has been updated!", "success")
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template("account.html", form=form)
