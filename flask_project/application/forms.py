from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.fields.core import DateField
from wtforms.validators import DataRequired, Length


class Read_GamesForm(FlaskForm):
    title = SelectField('title')

class Add_GamesForm(FlaskForm):
    title = StringField('Enter the Title          -',
        validators = [DataRequired(), Length(min=1, max=30)])
    genre = StringField('Enter the Genre:         -',
        validators = [DataRequired(), Length(min=1, max=30)])
    rating = StringField('Enter the Age Rating:   -',
        validators = [DataRequired(), Length(min=1, max=30)])
    devs = StringField('Enter the games Developer:-',
        validators = [DataRequired(), Length(min=1, max=30)])
    submit = SubmitField('Add your game to create a mission!')

class Add_Mission_list(FlaskForm):
    checkbox = BooleanField()
    mission_text = StringField('Enter your mission here!',
        validators = [DataRequired(), Length(min=2, max=200)])
    date = DateField()
    submit_mission = SubmitField ('Submit')



    # def validate_title(self, title):
    #     games = Games.query.all()
    #     if title == games.data:
    #         raise ValidationError('This game exists already!')

# class OrderGames(FlaskForm):
#     order_with = SelectField('Order With',
#         choices=[
#             ("complete", "Completed"),
#             ("id", "Recent"),
#             ("old", "Old"),
#             ('incomplete', "Incomplete")
#         ]
#     )
#     submit = SubmitField('Order')