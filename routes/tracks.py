from flask import Blueprint, jsonify
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from controllers.tracks import getTracks, getTrack, createTrack, updateTrack, deleteTrack

tracks_bp = Blueprint('tracks', __name__)


@tracks_bp.route('/tracks')
def readTracks():
    tracks = getTracks()
    return jsonify({'tracks': tracks})


@tracks_bp.route('/tracks/<string:id>')
def readTrack(id):
    track = getTrack(id)
    return jsonify({'track': track})


@tracks_bp.route('/tracks', methods=['POST'])
def createTracks():
    try:
        trackCreated = createTrack()
        return jsonify({'message': 'Tracks created succesfully', 'track': trackCreated}), 201

    except IntegrityError as err:
        print('track not created', err)
        return {'message': 'There is already an track with the same id'}, 400


@tracks_bp.route('/tracks/<string:id>', methods=['PUT'])
def updateTracks(id):
    try:
        trackUpdatep = updateTrack(id)
        return jsonify({'message': 'Tracks updated succesfully', 'track': trackUpdatep})

    except AttributeError as err:
        return {'message': 'Track not found'}, 404


@tracks_bp.route('/tracks/<string:id>', methods=['DELETE'])
def deleteTracks(id):
    try:
        deleteTrack(id)
        return jsonify({'message': 'Tracks deleted succesfully', 'track_id': id})

    except UnmappedInstanceError as err:
        return {'message': 'Track not found'}, 404

    except IntegrityError as err:
        return {'message': 'Cannot delete track is releated to someone.'}, 400
