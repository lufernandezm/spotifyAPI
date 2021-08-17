from flask import request
from models.artists import Artist
from models.genres import Genre
from models.db import db
from schemes.artists import artistSchema

artists_schema = artistSchema(many=True)
artist_schema = artistSchema()


def getArtists():
    artists = Artist.query.all()
    artistsFound = artists_schema.dump(artists)

    return artistsFound


def getArtist(id):
    artist = Artist.query.get(id)
    artistFound = artist_schema.dump(artist)

    return artistFound


def createArtist():
    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    followers = request.json["followers"],
    popularity = request.json["popularity"],
    img = request.json["img"],
    genres = request.json["genres"]

    new_artist = Artist(id, name, uri, url, href, followers, popularity, img)
    db.session.add(new_artist)
    db.session.commit()

    if len(genres) > 0:
        for i in range(len(genres)):
            genre_name = genres[i]
            genre = Genre.query.filter_by(name=genre_name).first()
            new_artist.relate_genre.append(genre)
            db.session.commit()

    artistCreated = artist_schema.dump(new_artist)
    return artistCreated


def updateArtist(id):
    artist = Artist.query.get(id)
    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    followers = request.json["followers"],
    popularity = request.json["popularity"],
    img = request.json["img"]

    artist.id = id
    artist.name = name
    artist.uri = uri
    artist.url = url
    artist.href = href
    artist.followers = followers
    artist.popularity = popularity
    artist.img = img

    db.session.commit()
    artistUpdatep = artist_schema.dump(artist)

    return artistUpdatep


def deleteArtist(id):
    artist = Artist.query.get(id)
    db.session.delete(artist)
    db.session.commit()