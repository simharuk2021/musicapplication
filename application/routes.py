from application import app, db
from application.models import Music, Artist, AddArtistForm, AddMusicForm
from flask import render_template, redirect, url_for, request

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 600 
app.config['SQLALCHEMY_POOL_RECYCLE'] = 100

# This is the route to the main page.

@app.route('/')
def home():
    return render_template('index.html')

''' This is the route to the add artist page. The code uses the AddArtistForm class to create a form.
Data is then passed to the database and the artist is added.  The index form is then rendered with an added message on success.'''

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

'''This route allows for tracks to be added to the database.  The AddMusicForm class is used to create the form
The Artist choices are populated from the database and returned as a selectfield so track names can be added to the correct artist.'''

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

# This route allows for a playlist to be displayed showing all of the tracks and artists in the database.  

@app.route('/music_list')
def tracks():
    all_music = Music.query.all()

    return render_template('music_list.html', all_music=all_music)

'''create a route to delete music from the database, this route is linked to a button which is 
rendered from the music_list page and is activated''' 

@app.route('/delete/<track_name>', methods = ['GET', 'DELETE'])
def delete(track_name):
    delete_music = Music.query.filter_by(track_name=track_name).first()
    db.session.delete(delete_music)
    db.session.commit()
    return redirect(url_for('tracks'))

#creates a route to display all of the artists in the database by query all()

@app.route('/edit_artists')
def edit():
    all_artists = Artist.query.all()
    return render_template('edit_artists.html', all_artists=all_artists)

'''creates a route to select the artist name to edit.  The specidic artist is selected and the add artist form
is rendered.  The name is updated by te User and this is sent to the database - the list of all artists view is then returned'''

@app.route('/edit_one_artist/<artist_name>', methods = ['GET', 'POST'])
def edit_artist(artist_name):
    form = AddArtistForm()
    edit_one_artist = Artist.query.filter_by(artist_name=artist_name).first()
    if request.method == 'POST':
        if edit_one_artist:
            edit_one_artist.artist_name = form.artist_name.data
            db.session.commit()
            return redirect(url_for('edit', message ="Artist Name Updated!"))
    else:
        return render_template('edit_one_artist.html', edit_one_artist=edit_one_artist, form=form)
