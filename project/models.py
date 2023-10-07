from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String())
