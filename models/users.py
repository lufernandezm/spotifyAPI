from models.db import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(30), primary_key=True, unique=True)
    name = db.Column(db.String(45))
    uri = db.Column(db.String(45))
    url = db.Column(db.String(45))
    href = db.Column(db.String(45))
    followers = db.Column(db.Integer, nullable=True)
    img = db.Column(db.String(45), nullable=True)
    playlists = db.relationship('Playlist', backref='relate_user')

    def __init__(self, id, name, uri, url, href, followers, img):
        self.id = id
        self.name = name
        self.uri = uri
        self.url = url
        self.href = href
        self.followers = followers
        self.img = img
