from application import app, db
from application.models import Music
from flask import render_template, redirect, url_for, request

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/add')
# def add():
#     new_game = Games(name="New Game")
#     db.session.add(new_game)
#     db.session.commit()
#     return "Added new game to database"

@app.route('/tracks')
def tracks():
    all_music = Music.query.all()
    # music_string = ""
    # for music in all_music:
    #     music_string += "<br>"+ music.track_name
    return render_template('tracks.html', all_music=all_music)

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name

# '''create a update route'''
# def delete(name):
#     music = Music.query.filter_by(track_name=name).first()
#     music.track_name = name
#     db.session.commit()
#     return music.track_name

# @app.route('/delete/<name>')