from flask import request
from models.albums import Album
from models.artists import Artist
from models.db import db
from schemes.albums import albumSchema

albums_schema = albumSchema(many=True)
album_schema = albumSchema()


def getAlbums():
    albums = Album.query.all()
    albumsFound = albums_schema.dump(albums)
    return albumsFound


def getAlbum(id):
    album = Album.query.get(id)
    albumFound = album_schema.dump(album)

    return albumFound


def createAlbum():
    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    total_tracks = request.json["total_tracks"],
    popularity = request.json["popularity"],
    img = request.json["img"]
    label = request.json["label"]
    release_date = request.json["release_date"]
    artists = request.json["artists"]

    new_album = Album(id, name, uri, url, href, total_tracks, popularity, img, label, release_date)
    db.session.add(new_album)
    db.session.commit()

    if len(artists) > 0:
        for i in range(len(artists)):
            artist_id = artists[i]
            artist = Artist.query.get(artist_id)
            new_album.relate_artist.append(artist)
            db.session.commit()

    albumCreated = album_schema.dump(new_album)

    return albumCreated


def updateAlbum(id):
    album = Album.query.get(id)

    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    total_tracks = request.json["total_tracks"],
    popularity = request.json["popularity"],
    img = request.json["img"]
    label = request.json["label"]
    release_date = request.json["release_date"]
    artists = request.json["artists"]

    album.id = id
    album.name = name
    album.uri = uri
    album.url = url
    album.href = href
    album.total_tracks = total_tracks
    album.popularity = popularity
    album.img = img
    album.label = label
    album.release_date = release_date

    db.session.commit()

    # for artist in album.relate_artist:
    #     print('artist name', artist.name)
        # db.session.delete(artist)
        # db.session.commit()

    # if len(artists) > 0:
    #     for i in range(len(artists)):
    #         artist_id = artists[i]
    #         artist = Artist.query.get(artist_id)
    #         Artist.children.remove(album)
    #         db.session.commit()

    albumUpdatep = album_schema.dump(album)

    return albumUpdatep


def deleteAlbum(id):
    album = Album.query.get(id)
    db.session.delete(album)
    db.session.commit()
