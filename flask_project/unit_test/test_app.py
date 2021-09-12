from application import app, db
from application.models import Games, Mission_List
from flask import url_for
from flask_testing import TestCase
from datetime import datetime


class TestBase(TestCase):

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        db.create_all()
        game = Games(title="Crash Bandicoot", genre="Action", rating="PG", devs="NaughtyDog")
        db.session.add(game)
        db.session.commit()

        mission = Mission_List(mission_text="Test text", date=datetime(2020, 4, 27, 0, 0, 0))
        db.session.add(mission)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

#lines 8
class TestHome(TestBase):
    def test_home(self):
        response = self.client.get(url_for('add'))
        self.assertEqual(response.status_code, 200)
#lines 26-28
class TestViewsGame(TestBase):
    def test_view_games(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Crash Bandicoot', response.data)
#lines 12-20
class TestAddGame(TestBase):
    def test_add_game(self):
        response = self.client.post(
            url_for('add'),
            data = dict(title="Test", genre="Test", rating="Test", devs="Test"),
            follow_redirects=True
        )
        self.assertIn(b'read',response.data)
#lines 58-61
class TestViewMission(TestBase):
    def test_view_mission(self):
        response = self.client.get(url_for('display_game', id=1), )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Crash Bandicoot', response.data)
#lines 79-86
class TestMissionText(TestBase):
    def test_add_text(self):
        response = self.client.post(
            url_for('add_text', id=1),
            data = dict(mission_text="Test Text2", date="2020, 4, 27, 0, 0, 0"),
            follow_redirects=True
        )
        self.assertIn(b'Test Text2',response.data)
#lines 97-98
class TestViewMission(TestBase):
    def test_view_mission(self):
        response = self.client.get(url_for('update_mission', id=1, game_id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test text', response.data)

class TestMissionUpdate(TestBase):
    def test_update_mission(self):
        response = self.client.post(
            url_for('update_mission', id=1, game_id=1),
            data = dict(mission_text="Test Text3", date="2020, 4, 27, 0, 0 ,0"),
            follow_redirects=True
        )
        self.assertIn(b'Test Text3', response.data)
#lines 103-105        
class TestDeleteText(TestBase):
    def test_delete_mission(self):
        response = self.client.get(url_for('mission_delete', id=1, game_id=1),
            follow_redirects=True
        )
        self.assertNotIn(b'Test Text', response.data)

class TestUpdateGame(TestBase):
    def test_view_update(self):
        response = self.client.get(url_for('update_game', id=1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Crash Bandicoot', 'Adventure', 'PG',  'Naughty Dog', response.data)

class TestUpdateGame(TestBase):
    def test_update_game(self):
        response = self.client.post(
            url_for('update_game', id=1),
            data = dict(title="Test", genre="Test", rating="Test", devs="Test"),
            follow_redirects=True
        )
        self.assertIn(b'Test',response.data)

class TestDeleteGame(TestBase):
    def test_delete_games(self):
        response = self.client.get(url_for('game_delete',id=1),
            follow_redirects=True
        )
        self.assertNotIn(b'Crash Bandicoot', response.data)

