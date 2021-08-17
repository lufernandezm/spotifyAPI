from flask import request
from models.genres import Genre
from models.db import db
from schemes.genres import genreSchema
from sqlalchemy.exc import IntegrityError

genres_schema = genreSchema(many=True)
genre_schema = genreSchema()


def getGenres():
    genres = Genre.query.all()
    genresFound = genres_schema.dump(genres)

    return genresFound


def getGenre(id):
    genre = Genre.query.get(id)
    genreFound = genre_schema.dump(genre)

    return genreFound


def createGenre():
    name = request.json["name"]
    genre = Genre.query.filter_by(name=name).first()

    if genre is None:
        new_genre = Genre(name)
        db.session.add(new_genre)
        db.session.commit()
        genreCreated = genre_schema.dump(new_genre)
        return genreCreated

    else:
        raise IntegrityError(None, None, None)


def updateGenre(id):
    genre = Genre.query.get(id)
    name = request.json["name"]

    genre.name = name

    db.session.commit()
    genreUpdatep = genre_schema.dump(genre)

    return genreUpdatep


def deleteGenre(id):
    genre = Genre.query.get(id)
    db.session.delete(genre)
    db.session.commit()
