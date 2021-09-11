from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Games, Mission_List
from application.forms import Add_GamesForm, Add_Mission_list

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app