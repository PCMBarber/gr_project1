from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.py"
app.config['SECRET_KEY'] = "secret-key"

db = SQLAlchemy(app)


from application import routes