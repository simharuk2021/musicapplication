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

@app.route('/music_list')
def tracks():
    all_music = Music.query.all()

    return render_template('music_list.html', all_music=all_music)

#create a route to delete music from the database
@app.route('/delete/<track_name>', methods = ['GET', 'DELETE'])
def delete(track_name):
    delete_music = Music.query.filter_by(track_name=track_name).first()
    db.session.delete(delete_music)
    db.session.commit()
    return redirect(url_for('tracks'))
    
@app.route('/edit_artists')
def edit():
    all_artists = Artist.query.all()

    return render_template('edit_artists.html', all_artists=all_artists)

@app.route('/edit_one_artist/<artist_name>', methods = ['GET', 'POST'])
def edit_artist(artist_name):
    form = AddArtistForm()
    edit_one_artist = Artist.query.filter_by(artist_name=artist_name).first()
    if request.method == 'POST':
        if edit_one_artist:
            edit_one_artist.artist_name = form.artist_name.data
            db.session.commit()
            return redirect(url_for('edit_artists', message ="Artist Name Updated!"))
    else:
        return render_template('edit_one_artist.html', edit_one_artist=edit_one_artist, form=form)

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