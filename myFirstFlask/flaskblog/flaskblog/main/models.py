from datetime import datetime
from flaskblog import db


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), unique=True, nullable=False)
  email = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(50), nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  posts = db.relationship('Post', backref='author', lazy=True)    # Build relationship with 'Post' model class
  
  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), nullable=False)
  content = db.Column(db.Text, nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)   # Reference with [table_name.column_name] to build foreign key

  def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}')"
