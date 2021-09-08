from flask import render_template, url_for, redirect, request
from application import app, db
from .models import Games, Mission_List
from .forms import Add_GamesForm, Add_Mission_list
from datetime import date


@app.route('/')
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
        db.session.add(mission)
        db.session.commit()
    games = Games.query.filterby(game_id=gameid)
    return render_template('mission_list.html', form = form, games = games)

@app.route('/display_game/<int:gameid>')
def display_game(gameid):
    games = Games.query.filterby(game_id=gameid)
    mission = Mission_List.query.filterby(game_id=gameid)
    return render_template('mission_list.html', games=games, mission=mission)

@app.route('/complete/<int:gameid>')
def complete(gameid):
    mission = Mission_List.query.get(gameid)
    mission.checklist = True
    db.session.commit()
    return redirect(url_for('display_game', gameid = gameid))

@app.route('/incomplete/<int:gameid>')
def incomplete(gameid):
    mission = Mission_List.query.get(gameid)
    mission.checklist = False
    db.session.commit()
    return redirect(url_for('display_game', gameid = gameid))

@app.route('/update_mission/<int:gameid>', methods= ['GET','POST'])
def update_mission(gameid):
    games = Mission_List.query.get(gameid)
    form = Add_Mission_list()
    if form.validate_on_submit():
        games.mission_text = form.mission_text.data
        db.session.commit()
        redirect(url_for('mission_list.html'))
    elif request.method == 'GET':
        form.mission_text.data = games.mission_text
    return render_template('mission_list.html', form=form, games=games)

@app.route('/delete/<int:id>')
def mission_delete(id):
    mission_text = Mission_List.query.get(id)
    db.session.delete(mission_text)
    db.session.commit()
    return redirect(url_for('mission_list.html', mission_text=mission_text))

