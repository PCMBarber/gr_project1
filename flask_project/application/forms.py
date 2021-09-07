from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, Length
from application.models import Games, Mission_List


# class Add_GamesForm(FlaskForm):
#     game = StringField('Add a game here',
#         validators = [DataRequired(), Length(min=1, max=30)])
#     submit = SubmitField('Games List')

#     def validate_title(self, game):
#         games = Games.query.all()
#         for game in games:
#             if game == game.data:
#                 raise ValidationError('This game exists already!')

# class OrderTodo(FlaskForm):
#     order_with = SelectField('Order With',
#         choices=[
#             ("complete", "Completed"),
#             ("id", "Recent"),
#             ("old", "Old"),
#             ('incomplete', "Incomplete")
#         ]
#     )
#     submit = SubmitField('Order')