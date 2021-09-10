from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Games, Mission_List

class TestBase(TestCase):

    def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
                # Create table
        db.create_all()
        # Create test games
        sample1 = Games(title="Crash Bandicoot", genre="Action", rating="PG", devs="NaughtyDog")
        # save games to database
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        # Close the database session and remove all contents of the database
        db.drop_all()

# Write a test class to test Read functionality
class TestViewsGame(TestBase):
    def test_view_games(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Crash Bandicoot', response.data)

class TestAddGame(TestBase):
    def test_add_games(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Crash Bandicoot', response.data)

class TestDeleteGame(TestBase):
    def test_delete_games(self):
        response = self.client.get(url_for('game_delete'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Crash Bandicoot', response.data)











# datetime(2020, 4, 27, 0, 0, 0)


# run this when you need to test
# # pytest --cov-report term-missing --cov=application test/