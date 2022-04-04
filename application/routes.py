from application import app, db
from application.models import Music

# @app.route('/add')
# def add():
#     new_game = Games(name="New Game")
#     db.session.add(new_game)
#     db.session.commit()
#     return "Added new game to database"

@app.route('/read')
def read():
    all_music = Music.query.all()
    music_string = ""
    for music in all_music:
        music_string += "<br>"+ music.track_name
    return music_string

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name