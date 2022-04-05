from application import db
from application import models
db.drop_all()
db.create_all()

# testartist = Artist(artist_name='Metallica') 
# Extra: this section populates the table with an example entry
# db.session.add(testartist)
# db.session.commit()

# testtrack = Music(track_name='My Symphony of You', artist_id = 1) # Extra: this section populates the table with an example entry
# db.session.add(testtrack)
# db.session.commit()

# testtrack2 = Music(track_name='Shivers', artist_id = 1) # Extra: this section populates the table with an example entry
# db.session.add(testtrack2)
# db.session.commit()