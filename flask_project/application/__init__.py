from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
#('SECRET_KEY')
#'sqlite:///app.db'
db = SQLAlchemy(app)

from application import routes
