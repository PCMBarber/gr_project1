from application import db

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    genre = db.Column(db.String(40), nullable=False)
    rating = db.Column(db.String(40), nullable=False)
    devs = db.Column(db.String(40), nullable=False)
    mission_link = db.relationship('Mission_List', backref=db.backref('link', lazy=True))

class Mission_List(db.Model):
    mission_id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    mission_text = db.Column(db.String(200))
    #checklist = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime)

