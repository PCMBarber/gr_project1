from flask import render_template, url_for, redirect, request
from application import app, db
from .models import Games, Mission_List
from .forms import Add_GamesForm, Add_Mission_list
from datetime import date

#this is the section you add your game to the game table
@app.route('/', methods=['GET', 'POST'])
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
        return redirect(url_for('read'))
    return render_template('add_game.html', form = form)

#This is the section where you read games from 
@app.route('/read_games')
def read():
    games = Games.query.all()
    return render_template('games_list.html', games = games)

@app.route('/update_games/<int:id>', methods= ['GET','POST'])
def update_game(id):
    games = Games.query.get(id)
    form = Add_GamesForm()
    if form.validate_on_submit():
        games.title = form.title.data
        games.genre = form.genre.data
        games.rating = form.rating.data
        games.devs = form.devs.data
        db.session.commit()
        return redirect(url_for('read'))
    elif request.method == 'GET':
        form.title.data = games.title
        form.genre.data = games.genre
        form.rating.data = games.rating
        form.devs.data = games.devs
    return render_template('update_games.html', form=form)

@app.route('/delete/<int:id>')
def game_delete(id):
    game_text = Games.query.get(id)
    db.session.delete(game_text)
    db.session.commit()
    return redirect(url_for('read', game_text=game_text))

#this is where you add your missions to the missions table

@app.route('/display_games/<int:id>', methods=['GET', 'POST'])
def display_game(id):
    form = Add_Mission_list()
    games = Games.query.filter_by(id=id).first()
    missions = Mission_List.query.filter_by(game_id=id).all()
    return render_template('mission_list.html', games=games, missions=missions, form=form)

# @app.route('/complete/<int:id>')
# def complete(id):
#     mission = Mission_List.query.get(id)
#     mission.checklist = True
#     db.session.commit()
#     return redirect(url_for('display_game', id = id))

# @app.route('/incomplete/<int:id>')
# def incomplete(id):
#     mission = Mission_List.query.get(id)
#     mission.checklist = False
#     db.session.commit()
#     return redirect(url_for('display_game', id = id))

@app.route('/submit_text/<int:id>', methods= ['GET', 'POST'])
def add_text(id):
    form = Add_Mission_list()
    games = Games.query.filter_by(id=id).first()
    missions = Mission_List.query.filter_by(game_id=id).all()
    if request.method == 'POST':
        mission_text = Mission_List(game_id = id, mission_text = form.mission_text.data, date = date.today())
        db.session.add(mission_text)
        db.session.commit()
        return redirect(url_for('add_text', id=id))
    return render_template('mission_list.html', games=games, missions=missions, form=form)

@app.route('/update_mission/<int:id>/<int:game_id>', methods= ['GET','POST'])
def update_mission(id, game_id):
    game = Mission_List.query.get(id)
    form = Add_Mission_list()
    if form.validate_on_submit():
        game.mission_text = form.mission_text.data
        db.session.commit()
        return redirect(url_for('submit_text', id = game_id))
    elif request.method == 'GET':
        form.mission_text.data = game.mission_text
    return render_template('update_mission.html', form=form)

@app.route('/delete_mission/<int:id>/<int:game_id>')
def mission_delete(id, game_id):
    mission_text = Mission_List.query.get(id)
    db.session.delete(mission_text)
    db.session.commit()
    return redirect(url_for('add_text', id=game_id))

