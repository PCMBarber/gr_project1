from application import db

class Games(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), Nullable=False)
    genre = db.Column(db.String(40), Nullable=False)
    age_rating = db.Column(db.String(40), Nullable=False)
    dev_studio = db.Column(db.String(40), Nullable=False)


class Mission_List(db.Model):

    mission_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('Games'))
    mission_text = db.Column(db.String(200))
    checklist = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime)