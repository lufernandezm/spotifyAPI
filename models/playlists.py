from models.db import db


class Playlist(db.Model):
    __tablename__ = 'playlists'
    id = db.Column(db.String(30), primary_key=True, unique=True)
    name = db.Column(db.String(45))
    uri = db.Column(db.String(45))
    url = db.Column(db.String(45))
    href = db.Column(db.String(45))
    description = db.Column(db.Text, nullable=True)
    followers = db.Column(db.Integer, nullable=True)
    img = db.Column(db.String(45), nullable=True)
    user_id = db.Column(db.String(30), db.ForeignKey('users.id'))

    def __init__(self, id, name, uri, url, href, description, followers, img, user_id):
        self.id = id
        self.name = name
        self.uri = uri
        self.url = url
        self.href = href
        self.description = description
        self.followers = followers
        self.img = img
        self.user_id = user_id
