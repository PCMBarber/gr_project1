from application import db


# this is my models/schema for the project

class Games(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(40), Nullable=False)

    genre = db.Column(db.String(40), Nullable=False)

    age_rating = db.Column(db.String(40), Nullable=False)

    dev_studio = db.Column(db.String(40), Nullable=False)

class Missions(db.Model):

    mission_id = db.Column(db.Integer, primary_key=True)

    game_id = db.Column(db.Integer, db.ForeignKey())

    mission_text = db.Column(db.String(40), Nullable=True)

    checklist = db.Column(db.Boolean, deault=False)

    date = db.Column(db.DateTime)