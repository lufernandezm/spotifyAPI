from flask import Blueprint, jsonify
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import FlushError
from controllers.albums import getAlbums, getAlbum, createAlbum, updateAlbum, deleteAlbum

albums_bp = Blueprint('albums', __name__)


@albums_bp.route('/albums')
def readAlbums():
    albums = getAlbums()
    return jsonify({'albums': albums})


@albums_bp.route('/albums/<string:id>')
def readAlbum(id):
    album = getAlbum(id)
    return jsonify({'album': album})


@albums_bp.route('/albums', methods=['POST'])
def createAlbums():
    try:
        albumCreated = createAlbum()
        return jsonify({'message': 'Albums created succesfully', 'album': albumCreated}), 201

    except IntegrityError as err:
        print('album not created', err)
        return {'message': 'There is already an album with the same id'}, 400

    except FlushError as err:
        print('album not created', err)
        return {'message': 'Artist(s) id does not exist.'}, 400


@albums_bp.route('/albums/<string:id>', methods=['PUT'])
def updateAlbums(id):
    try:
        albumUpdatep = updateAlbum(id)
        return jsonify({'message': 'Albums updated succesfully', 'album': albumUpdatep})

    except AttributeError as err:
        print('album not founded', err)
        return {'message': 'Album not found'}, 404


@albums_bp.route('/albums/<string:id>', methods=['DELETE'])
def deleteAlbums(id):
    try:
        deleteAlbum(id)
        return jsonify({'message': 'Albums deleted succesfully', 'album_id': id})

    except UnmappedInstanceError as err:
        print('album not founded', err)
        return {'message': 'Album not found'}, 404

    except IntegrityError as err:
        return {'message': 'Cannot delete album is releated to someone.'}, 400
