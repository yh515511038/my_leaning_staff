from datetime import datetime
from flaskblog import db


class User(db.Model):
  id = db.column(db.Integer, nullable=False, primary_key = True)
  username = db.column(db.String(50), nullable=False)
  email = db.column(db.String(50), nullable=False)
  password = db.column(db.String(50), nullable=False)
  image_file = db.column(db.String(20), nullable=False, default='default.jpg')


class Post(db.Model):
  name = db.column(db.String(50), nullable=False)
  author = db.column(db.String(50), nullable=False)
  text = db.column(db.Text, nullable=False)
  created = db.column(db.Datetime, nullable=False, default=datetime.utcnow)
