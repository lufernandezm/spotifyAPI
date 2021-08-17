from flask import request
from models.playlists import Playlist
from models.tracks import Track
from models.db import db
from schemes.playlists import playlistSchema

playlists_schema = playlistSchema(many=True)
playlist_schema = playlistSchema()


def getPlaylists():
    playlists = Playlist.query.all()
    playlistsFound = playlists_schema.dump(playlists)

    return playlistsFound


def getPlaylist(id):
    playlist = Playlist.query.get(id)
    playlistFound = playlist_schema.dump(playlist)

    return playlistFound


def createPlaylist():
    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    followers = request.json["followers"],
    description = request.json["description"],
    img = request.json["img"],
    user_id = request.json["user_id"],
    tracks = request.json["tracks"]

    new_playlist = Playlist(id, name, uri, url, href, followers, description, img, user_id)

    db.session.add(new_playlist)
    db.session.commit()

    if len(tracks) > 0:
        for i in range(len(tracks)):
            track_id = tracks[i]
            track = Track.query.get(track_id)
            new_playlist.relate_track.append(track)
            db.session.commit()

    playlistCreated = playlist_schema.dump(new_playlist)
    return playlistCreated


def updatePlaylist(id):
    playlist = Playlist.query.get(id)
    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    followers = request.json["followers"],
    description = request.json["description"],
    img = request.json["img"],
    user_id = request.json["user_id"]

    playlist.id = id
    playlist.name = name
    playlist.uri = uri
    playlist.url = url
    playlist.href = href
    playlist.followers = followers
    playlist.description = description
    playlist.img = img
    playlist.user_id = user_id

    db.session.commit()
    playlistUpdatep = playlist_schema.dump(playlist)

    return playlistUpdatep


def deletePlaylist(id):
    playlist = Playlist.query.get(id)
    db.session.delete(playlist)
    db.session.commit()
