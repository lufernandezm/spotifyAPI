from flask import Blueprint, jsonify
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from controllers.genres import getGenres, getGenre, createGenre, updateGenre, deleteGenre

genres_bp = Blueprint('genres', __name__)


@genres_bp.route('/genres')
def readGenres():
    genres = getGenres()
    return jsonify({'genres': genres})


@genres_bp.route('/genres/<string:id>')
def readGenre(id):
    genre = getGenre(id)
    return jsonify({'genre': genre})


@genres_bp.route('/genres', methods=['POST'])
def createGenres():
    try:
        genreCreated = createGenre()
        return jsonify({'message': 'Genres created succesfully', 'genre': genreCreated}), 201

    except IntegrityError as err:
        print('genre not created', err)
        return {'message': 'There is already an genre with the same id'}, 400


@genres_bp.route('/genres/<string:id>', methods=['PUT'])
def updateGenres(id):
    try:
        genreUpdatep = updateGenre(id)
        return jsonify({'message': 'Genres updated succesfully', 'genre': genreUpdatep})

    except AttributeError as err:
        return {'message': 'Genre not found'}, 404


@genres_bp.route('/genres/<string:id>', methods=['DELETE'])
def deleteGenres(id):
    try:
        deleteGenre(id)
        return jsonify({'message': 'Genres deleted succesfully', 'genre_id': id})

    except UnmappedInstanceError as err:
        return {'message': 'Genre not found'}, 404

    except IntegrityError as err:
        return {'message': 'Cannot delete genre is releated to someone.'}, 400
