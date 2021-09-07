from flask import render_template, url_for, redirect, request
from application import app, db
from .models import Games, Mission_List
from .forms import Add_GamesForm, Add_Mission_list
from datetime import date

@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/add_game', methods=['GET', 'POST'])
def add():
    form = Add_GamesForm()
    if request.method == 'POST':
        new_title = form.title.data
        new_genre = form.genre.data
        new_rating = form.rating.data
        new_devs = form.devs.data
        game = Games(title=new_title, genre=new_genre, rating=new_rating, devs=new_devs)
    db.session.add(game)
    db.session.commit()
    return render_template('layout.html', form = form)

@app.route('/read_games')
def read():
    games = Games.query.all()
    return render_template('dropdown_games.html', games = games)

@app.route('/mission_text/<int:gameid>', methods=['GET','POST'])
def add_mission(gameid):
    form = Add_Mission_list()
    if request.method == 'POST':
        new_mission_text = form.mission_text.data
        new_date = date.today()
        mission = Mission_List(game_id=gameid, mission_text=new_mission_text, checklist=False, date=new_date)
    return render_template('mission_list.html', form = form)
