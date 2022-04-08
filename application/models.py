from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired

#creates the Artist class which is used to store artist data as a table within the database
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(45), nullable=False)
    music_artist = db.relationship('Music', backref='musicbr') 

    def __repr__(self):
        return 'Choose {}'.format(self.artist_name)

#creates the Music class which is used to store track data as a table within the database (using the artist id as a foreign key)
class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_name = db.Column(db.String(45), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)

#creates the AddArtistForm class which is used to create the form for adding artists    
class AddArtistForm(FlaskForm):
    artist_name = StringField('Artist Name', validators=[DataRequired()])
    submit = SubmitField('Add Name!')

#creates the AddMusicForm class which is used to create the form for adding tracks
class AddMusicForm(FlaskForm):
    track_name = StringField('Track Name', validators=[DataRequired()])
    artist_name = SelectField(u'Artist Name', choices = [])
    submit = SubmitField('Add Track!')


