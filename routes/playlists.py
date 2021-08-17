from flask import Blueprint, jsonify
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from controllers.playlists import getPlaylists, getPlaylist, createPlaylist, updatePlaylist, deletePlaylist

playlists_bp = Blueprint('playlists', __name__)


@playlists_bp.route('/playlists')
def readPlaylists():
    playlists = getPlaylists()
    return jsonify({'playlists': playlists})


@playlists_bp.route('/playlists/<string:id>')
def readPlaylist(id):
    playlist = getPlaylist(id)
    return jsonify({'playlist': playlist})


@playlists_bp.route('/playlists', methods=['POST'])
def createPlaylists():
    try:
        playlistCreated = createPlaylist()
        return jsonify({'message': 'Playlists created succesfully', 'playlist': playlistCreated}), 201

    except IntegrityError as err:
        print('playlist not created', err)
        return {'message': 'There is already an playlist with the same id'}, 400


@playlists_bp.route('/playlists/<string:id>', methods=['PUT'])
def updatePlaylists(id):
    try:
        playlistUpdatep = updatePlaylist(id)
        return jsonify({'message': 'Playlists updated succesfully', 'playlist': playlistUpdatep})

    except AttributeError as err:
        return {'message': 'Playlist not found'}, 404


@playlists_bp.route('/playlists/<string:id>', methods=['DELETE'])
def deletePlaylists(id):
    try:
        deletePlaylist(id)
        return jsonify({'message': 'Playlists deleted succesfully', 'playlist_id': id})

    except UnmappedInstanceError as err:
        return {'message': 'Playlist not found'}, 404

    except IntegrityError as err:
        return {'message': 'Cannot delete playlist is releated to someone.'}, 400
