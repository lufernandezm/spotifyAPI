from models.db import db


class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.String(30), primary_key=True, unique=True)
    name = db.Column(db.String(45))
    uri = db.Column(db.String(45))
    url = db.Column(db.String(45))
    href = db.Column(db.String(45))
    total_tracks = db.Column(db.Integer)
    popularity = db.Column(db.Integer, nullable=True)
    img = db.Column(db.String(45), nullable=True)
    label = db.Column(db.String(45), nullable=True)
    release_date = db.Column(db.String(45))
    tracks = db.relationship('Track', backref='relate_album')

    def __init__(self, id, name, uri, url, href, total_tracks, popularity, img, label, release_date):
        self.id = id
        self.name = name
        self.uri = uri
        self.url = url
        self.href = href
        self.total_tracks = total_tracks
        self.popularity = popularity
        self.img = img
        self.label = label
        self.release_date = release_date
