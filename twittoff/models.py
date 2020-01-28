"""SQLAlcmemy models for twittoff"""

from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    """Twitter users for which we query and store historical tweets."""
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(15), unique=True, nullable=False)

class Tweets(DB.Model):
    """Stores tweets."""
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))

    
