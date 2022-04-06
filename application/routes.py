from application import app, db
from application.models import Music, Artist, AddArtistForm, AddMusicForm
from flask import render_template, redirect, url_for, request

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 600 
app.config['SQLALCHEMY_POOL_RECYCLE'] = 100

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_artist', methods = ['GET', 'POST'])
def add_artist():
    form = AddArtistForm()
    if form.validate_on_submit():
        new_artist = Artist(artist_name =form.artist_name.data)
        db.session.add(new_artist)
        db.session.commit()
        return render_template('index.html', message="Artist Added!")
    else:
        return render_template('add_artist.html', form=form)

@app.route('/add_music', methods = ['GET', 'POST'])
def add_music():
    form = AddMusicForm()
    form.artist_name.choices = [(artist.id, artist.artist_name) for artist in Artist.query.order_by(Artist.artist_name).all()]
    if form.validate_on_submit():
        new_track = Music(track_name =form.track_name.data, artist_id =form.artist_name.data)
        db.session.add(new_track)
        db.session.commit()
        return render_template('index.html', message="Track Added!")
    else:
        return render_template('add_music.html', form=form)

'''create a route which displays all the tracks in the database'''
@app.route('/music_list')   
def music_list():
    return render_template('music_list.html', music=Music.query.all())

    


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