from models.db import db

artists_genres = db.Table('artists_genres',
                          db.Column('genre_id', db.String(30), db.ForeignKey('genres.id')),
                          db.Column('artist_id', db.String(30), db.ForeignKey('artists.id'))
                          )


class Genre(db.Model):
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(45), unique=True)
    artist_genre = db.relationship('Artist', secondary=artists_genres, backref=db.backref('relate_genre'), lazy='dynamic')

    def __init__(self, name):
        self.name = name
