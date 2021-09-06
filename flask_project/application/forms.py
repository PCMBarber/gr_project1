from gr_project1.flask_project.application.models import Games
from gr_project1.flask_project.application.routes import games
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Todos
# add all the classes in here

class GamesForm(FlaskForm):
    game = StringField('Add a game here',
        validators = [DataRequired()])
    submit = SubmitField('Submit')

    def validate_task(self, game):
        games = Games.query.all()
        for game in games:
            if game.task == game.data:
                raise ValidationError('This game exists already!')

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