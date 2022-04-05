from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(45), nullable=False)
    music_artist = db.relationship('Music', backref='musicbr') 

    def __repr__(self):
        return 'Choose {}'.format(self.artist_name)

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_name = db.Column(db.String(45), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    
class AddArtistForm(FlaskForm):
    artist_name = StringField('Artist Name')
    submit = SubmitField('Add Artist!')

class AddMusicForm(FlaskForm):
    track_name = StringField('Track Name')
    artist_name = SelectField('Artist Name', coerce=int)
    submit = SubmitField('Add Track!')

