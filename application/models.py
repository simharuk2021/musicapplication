from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(45), nullable=False)
    music = db.relationship('Music', backref='musicbr') 

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_name = db.Column(db.String(45), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    

class AddArtistForm(FlaskForm):
    artist_name = StringField('Artist Name')
    # artist_id = QuerySelectField('Artist', query_factory=artist_query, allow_blank=True)
    submit = SubmitField('Add Artist!')