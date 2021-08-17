from flask import request
from models.tracks import Track
from models.artists import Artist
from models.db import db
from schemes.tracks import trackSchema

tracks_schema = trackSchema(many=True)
track_schema = trackSchema()


def getTracks():
    tracks = Track.query.all()
    tracksFound = tracks_schema.dump(tracks)

    return tracksFound


def getTrack(id):
    track = Track.query.get(id)
    trackFound = track_schema.dump(track)

    return trackFound


def createTrack():
    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    duration_ms = request.json["duration_ms"],
    popularity = request.json["popularity"],
    album_id = request.json["album_id"],
    artists = request.json["artists"]

    new_track = Track(id, name, uri, url, href, duration_ms, popularity, album_id)
    db.session.add(new_track)
    db.session.commit()

    if len(artists) > 0:
        for i in range(len(artists)):
            artist_id = artists[i]
            artist = Artist.query.get(artist_id)
            new_track.relate_artist.append(artist)
            db.session.commit()

    trackCreated = track_schema.dump(new_track)
    return trackCreated


def updateTrack(id):
    track = Track.query.get(id)
    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    duration_ms = request.json["duration_ms"],
    popularity = request.json["popularity"],
    album_id = request.json["album_id"]

    track.id = id
    track.name = name
    track.uri = uri
    track.url = url
    track.href = href
    track.duration_ms = duration_ms
    track.popularity = popularity
    track.album_id = album_id

    db.session.commit()
    trackUpdatep = track_schema.dump(track)

    return trackUpdatep


def deleteTrack(id):
    track = Track.query.get(id)
    db.session.delete(track)
    db.session.commit()
