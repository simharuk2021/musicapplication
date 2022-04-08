from application.models import Artist, Music, AddArtistForm, AddMusicForm
from flask_testing import TestCase
from application import app, db
from flask import url_for, render_template, request, redirect

class TestBase(TestCase):
    
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db', DEBUG=True, WTF_CSRF_ENABLED=False, SQLALCHEMY_POOL_TIMEOUT=None, SQLALCHEMY_TRACK_MODIFICATIONS=False)
        return app
        # from application import app
        # return app
    
    def setUp(self):
        db.create_all()
        new_artist = Artist(artist_name ="Test Artist")
        new_music = Music(track_name ="Test Track", artist_id =1)
        db.session.add(new_artist)
        db.session.add(new_music)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

        def test_home_get(self):
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Music', response.data)

        def test_home_add_artist(self):
            response = self.client.get(url_for('add_artist'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Add Artist', response.data)

class TestData(TestBase):

    def test_add_artist(self):
        response = self.client.post(url_for('add_artist'), data=dict(artist_name="Test Artist"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Artist Added!', response.data)
    
    def test_add_music(self):
        response = self.client.post('/add_music', data=dict(track_name="Test Track", artist_name=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Track Added!', response.data)
    
    def test_music_list(self):
        response = self.client.get('/music_list')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Artist', response.data)
        self.assertIn(b'Test Track', response.data)
    
    def test_delete(self):
        response = self.client.get('/delete/Test Track', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Current playlist', response.data)
    
    def test_add_artist_form(self):
        form = AddArtistForm()
        self.assertEqual(form.validate_on_submit(), False)

    def test_home_get2(self):
        response = self.client.get(url_for('edit'))
        assert"Test Artist" in response.data.decode()
