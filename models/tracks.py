from models.db import db

playlists_tracks = db.Table('playlists_tracks',
                            db.Column('track_id', db.String(30), db.ForeignKey('tracks.id')),
                            db.Column('playlist_id', db.String(30), db.ForeignKey('playlists.id'))
                            )


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.String(30), primary_key=True, unique=True)
    name = db.Column(db.String(45))
    uri = db.Column(db.String(45))
    url = db.Column(db.String(45))
    href = db.Column(db.String(45))
    duration_ms = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    album_id = db.Column(db.String(30), db.ForeignKey('albums.id'))
    playlist_track = db.relationship('Playlist', secondary=playlists_tracks, backref=db.backref('relate_track'), lazy=True)

    def __init__(self, id, name, uri, url, href, duration_ms, popularity, album_id):
        self.id = id
        self.name = name
        self.uri = uri
        self.url = url
        self.href = href
        self.duration_ms = duration_ms
        self.popularity = popularity
        self.album_id = album_id
