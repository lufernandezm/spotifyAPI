from models.db import db

albums_artists = db.Table('albums_artists',
                          db.Column('artist_id', db.String(30), db.ForeignKey('artists.id')),
                          db.Column('album_id', db.String(30), db.ForeignKey('albums.id'))
                          )

artists_tracks = db.Table('artists_tracks',
                          db.Column('track_id', db.String(30), db.ForeignKey('tracks.id')),
                          db.Column('artist_id', db.String(30), db.ForeignKey('artists.id'))
                          )


class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.String(30), primary_key=True, unique=True)
    name = db.Column(db.String(45))
    uri = db.Column(db.String(45))
    url = db.Column(db.String(45))
    href = db.Column(db.String(45))
    followers = db.Column(db.Integer, nullable=True)
    popularity = db.Column(db.Integer, nullable=True)
    img = db.Column(db.String(45), nullable=True)
    album_artist = db.relationship('Album', secondary=albums_artists, backref=db.backref('relate_artist'), lazy='dynamic')
    artist_track = db.relationship('Track', secondary=artists_tracks, backref=db.backref('relate_artist'), lazy='dynamic')

    def __init__(self, id, name, uri, url, href, followers, popularity, img):
        self.id = id
        self.name = name
        self.uri = uri
        self.url = url
        self.href = href
        self.followers = followers
        self.popularity = popularity
        self.img = img
