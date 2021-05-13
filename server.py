from flask import Flask, request, jsonify
from datetime import datetime
from sqlite3 import Connection as SQLite3Connection

# App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite.file"
app.config["SQL_TRACK_MODIFICATIONS"] = 0

# Models
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost")
