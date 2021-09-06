from flask import render_template, url_for, redirect, request
from application import app, db                     #the app and the database variable
from application.models import Games, Missions      #the name of my models
from application.forms import  GamesForm            #the name of my forms

@app.route('/')

@app.route('/games', methods=['GET', 'POST', 'PUT'])
def games():
    if request.method == 'POST':
        return 'Add a game here'
    else:
        return 'Look for a game?'

@app.route('/mission_text', methods=['GET', 'POST', 'PUT', 'DELETE'])
def games():
    if request.method == 'POST':
        return 'Add a review here'
    else:
        return 'Find the review'