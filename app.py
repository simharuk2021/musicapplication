# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import os

# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI") # environment variable was exported using below run in terminal: 


# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
# db = SQLAlchemy(app)

# # from application import db

# class Artist(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     artist_name = db.Column(db.String(45), nullable=False)
#     music = db.relationship('Music', backref='musicbr') 

# class Music(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     track_name = db.Column(db.String(45), nullable=False)
#     artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)



# class Artist_Music(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     artist_id = db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'))
#     music_id = db.Column('music_id', db.Integer, db.ForeignKey('music.id'))

from application import app

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')