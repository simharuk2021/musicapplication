from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired

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
    artist_name = StringField('Artist Name', validators=[DataRequired()])
    submit = SubmitField('Add Name!')

class AddMusicForm(FlaskForm):
    track_name = StringField('Track Name', validators=[DataRequired()])
    artist_name = SelectField(u'Artist Name', choices = [])
    submit = SubmitField('Add Track!')
def add_album(request, id):
    artist = Artist.query.get(id)
    form = ArtistDetails(request.POST, obj=artist)
    form.artist_id.choices = [(artist.id, artist.artist_name) for artist in Artist.query.order_by(artist_name)]


