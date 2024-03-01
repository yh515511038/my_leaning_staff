from flaskblog import db

class User(db.Model):
    username = db.Column("username", db.String)