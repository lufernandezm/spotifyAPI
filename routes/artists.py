from flask import Blueprint, jsonify
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError
from controllers.artists import getArtists, getArtist, createArtist, updateArtist, deleteArtist

artists_bp = Blueprint('artists', __name__)


@artists_bp.route('/artists')
def readArtists():
    artists = getArtists()
    return jsonify({'artists': artists})


@artists_bp.route('/artists/<string:id>')
def readArtist(id):
    artist = getArtist(id)
    return jsonify({'artist': artist})


@artists_bp.route('/artists', methods=['POST'])
def createArtists():
    try:
        artistCreated = createArtist()
        return jsonify({'message': 'Artists created succesfully', 'artist': artistCreated}), 201

    except IntegrityError as err:
        print('artist not created', err)
        return {'message': 'There is already an artist with the same id'}, 400

    except FlushError as err:
        print('album not created', err)
        return {'message': 'Genre(s) does not exist.'}, 400


@artists_bp.route('/artists/<string:id>', methods=['PUT'])
def updateArtists(id):
    try:
        artistUpdatep = updateArtist(id)
        return jsonify({'message': 'Artists updated succesfully', 'artist': artistUpdatep})

    except AttributeError as err:
        return {'message': 'Artist not found'}, 404


@artists_bp.route('/artists/<string:id>', methods=['DELETE'])
def deleteArtists(id):
    try:
        deleteArtist(id)
        return jsonify({'message': 'Artists deleted succesfully', 'artist_id': id})

    except UnmappedInstanceError as err:
        return {'message': 'Artist not found'}, 404

    except IntegrityError as err:
        return {'message': 'Cannot delete artist is releated to someone.'}, 400
