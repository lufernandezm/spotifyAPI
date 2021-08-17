from flask import jsonify, request
from models.users import User
from models.db import db
from schemes.users import userSchema

users_schema = userSchema(many=True)
user_schema = userSchema()


def getUsers():
    users = User.query.all()
    usersFound = users_schema.dump(users)

    return usersFound


def getUser(id):
    user = User.query.get(id)
    userFound = user_schema.dump(user)

    return userFound


def createUser():
    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    followers = request.json["followers"],
    img = request.json["img"]

    new_user = User(id, name, uri, url, href, followers, img)
    db.session.add(new_user)
    db.session.commit()
    userCreated = user_schema.dump(new_user)
    return userCreated


def updateUser(id):
    user = User.query.get(id)
    id = request.json["id"],
    name = request.json["name"],
    uri = request.json["uri"],
    url = request.json["url"],
    href = request.json["href"],
    followers = request.json["followers"],
    img = request.json["img"]

    user.id = id
    user.name = name
    user.uri = uri
    user.url = url
    user.href = href
    user.followers = followers
    user.img = img

    db.session.commit()
    userUpdatep = user_schema.dump(user)

    return userUpdatep


def deleteUser(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
