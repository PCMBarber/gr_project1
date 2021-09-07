from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.py"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)


# from application import forms
# from application import models
# from application import routes