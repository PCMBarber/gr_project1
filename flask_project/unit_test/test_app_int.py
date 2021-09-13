from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Games

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
        db.create_all()
        self.driver.get(f'http://localhost:{self.TEST_PORT}/add_game')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/add_game')
        self.assertEqual(response.code, 200)

class Test_Empty_Fields(TestBase):

    def test_empty_add_game(self):
        self.submit_input('')
        self.assertIn(url_for('add'), self.driver.current_url)

        text = self.driver.find_element_by_xpath('//*[@id="title"]').text
        self.assertIn("The name field can't be empty!", text)

        entries = Games.query.all()
        self.assertEqual(len(entries), 0)
    
    def test_empty_add_mission(self):
        self.submit_input('')
        self.assertIn(url_for('display'), self.driver.current_url)

        text = self.driver.find_element_by_xpath('//*[@id="title"]').text
        self.assertIn("The name field can't be empty!", text)

        entries = Games.query.all()
        self.assertEqual(len(entries), 0)

class Test_Click(TestBase):
    def submit_input(self):
        games = "test"
        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(games)
        self.driver.find_element_by_xpath('//*[@id="genre"]').send_keys(games)
        self.driver.find_element_by_xpath('//*[@id="rating"]').send_keys(games)
        self.driver.find_element_by_xpath('//*[@id="devs"]').send_keys(games)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()

class Test_View(TestBase):
    def test_server_addgame(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/add_game')
        self.assertEqual(response.code, 200)
    
    def test_server_selectgame(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/submit_text')
        self.assertEqual(response.code, 200)

    def test_server_(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}/display_game')
        self.assertEqual(response.code, 200)