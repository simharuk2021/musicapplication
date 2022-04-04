from application import app, db
from application.models import Music, Artist, AddArtistForm
from flask import render_template, redirect, url_for, request

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

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

@app.route('/add_artist', methods = ['GET','POST'])
def add_artist():
    form = AddArtistForm()
    if form.validate_on_submit():
        new_artist = Artist(artist_name =form.artist_name.data)
        db.session.add(new_artist)
        db.session.commit()
        return render_template('index.html', message="Artist Added!")
    else:
        return render_template('add_artist.html', form=form)

# @app.route('/addtrack', methods = ['GET', 'POST'])
# def add_track():
#     # instantiate the DogForm object
#     form = addTrack()
#     # if the form is valid, we want to add the dog to the database
#     if form.validate_on_submit():
#         # create a new dog object
#         new_track = Music(track_name=form.track_name.data)
#         # add the dog to the database
#         db.session.add(new_track)
#         # commit the changes to the database
#         db.session.commit()
#         # redirect to the home page
#         return redirect(url_for('tracks'))
#     # pass object to Jinja2 template
#     return render_template('add_track.html', form=form)

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