from flask import render_template, url_for, redirect, request
from application import app, db                     #the app and the database variable
from application.models import Games, Missions_List      #the name of my models
from application.forms import  GamesForm            #the name of my forms

@app.route('/')
def home():
    return render_template('layout.html')
# @app.route('/games_list', methods=['GET', 'POST'])
# def games():
    
#     if request.method == 'POST':
#         return 'Add a game here'
#     return render_template('layout.html', 'games.html')


# @app.route('/mission_text', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def games():
#     if request.method == 'POST':
#         return 'Add a review here'
#     else:
#         return 'Find the review'