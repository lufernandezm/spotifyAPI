from flask import Blueprint, jsonify
from sqlalchemy.orm.exc import UnmappedInstanceError
from sqlalchemy.exc import IntegrityError
from controllers.users import getUsers, getUser, createUser, updateUser, deleteUser

users_bp = Blueprint('users', __name__)


@users_bp.route('/users')
def readUsers():
    users = getUsers()
    return jsonify({'users': users})


@users_bp.route('/users/<string:id>')
def readUser(id):
    user = getUser(id)
    return jsonify({'user': user})


@users_bp.route('/users', methods=['POST'])
def createUsers():
    try:
        userCreated = createUser()
        return jsonify({'message': 'Users created succesfully', 'user': userCreated}), 201

    except IntegrityError as err:
        print('user not created', err)
        return {'message': 'There is already an user with the same id'}, 400


@users_bp.route('/users/<string:id>', methods=['PUT'])
def updateUsers(id):
    try:
        userUpdatep = updateUser(id)
        return jsonify({'message': 'Users updated succesfully', 'user': userUpdatep})

    except AttributeError as err:
        return {'message': 'User not found'}, 404


@users_bp.route('/users/<string:id>', methods=['DELETE'])
def deleteUsers(id):
    try:
        deleteUser(id)
        return jsonify({'message': 'Users deleted succesfully', 'user_id': id})

    except UnmappedInstanceError as err:
        return {'message': 'User not found'}, 404

