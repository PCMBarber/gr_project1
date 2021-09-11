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
    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all() # create schema before we try to get the page

        self.driver.get(f'http://localhost:{self.TEST_PORT}/add-question')

        def tearDown(self):
            self.driver.quit()

            db.drop_all()

        def test_server_is_up_and_running(self):
            response = urlopen(f'http://localhost:{self.TEST_PORT}/add-question')
            self.assertEqual(response.code, 200)
