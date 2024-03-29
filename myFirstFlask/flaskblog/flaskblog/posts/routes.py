from flask import Blueprint, request, flash, render_template, redirect, url_for
from flask_login import current_user, login_required

from flaskblog import db
from .forms import PostForm
from .models import Post


posts = Blueprint('posts', __name__)

@posts.route("/new_post/", methods=["GET", "POST"])
@login_required
def new_post():
  form = PostForm()
  if request.method == "POST" and form.validate_on_submit():
    new_post = Post(title=form.title.data, content=form.content.data, user_id=current_user.id)
    db.session.add(new_post)
    db.session.commit()
    flash("Your post has been posted!", "success")
    return redirect(url_for("main.home"))
  elif request.method == "GET":
    return render_template("new_post.html", form=form, title="New Post")


@posts.route("/post/<int:id>")
def post(id):
  post = Post.query.get(id)
  return render_template("post.html", post=post)


@posts.route("/update_post/<int:id>", methods=["GET", "POST"])
def update_post(id):
  post = Post.query.get(id)
  form = PostForm()
  if request.method == "POST" and form.validate_on_submit():
    post.title = form.title.data
    post.content = form.content.data
    db.session.commit()
    flash("Your post has been updated!", "success")
  elif request.method == "GET":
    form.title.data = post.title
    form.content.data = post.content
  return render_template("new_post.html", form=form, title="Update Post")


@posts.route("/delete_post/<int:id>", methods=["GET", "POST"])
def delete_post(id):
  post = Post.query.get(id)
  db.session.delete(post)
  db.session.commit()
  flash("Your post has been deleted!", "success")
  return redirect(url_for("main.home"))
