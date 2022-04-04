from application import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(45), nullable=False)
    music = db.relationship('Music', backref='musicbr') 

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_name = db.Column(db.String(45), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)