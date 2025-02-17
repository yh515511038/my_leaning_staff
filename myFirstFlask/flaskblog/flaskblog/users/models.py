from flask_login import UserMixin
from flaskblog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    image_file = db.Column(db.String(50), default='default.jpg')
    post = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"{self.username} - {self.email}"
