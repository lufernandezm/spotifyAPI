from flask import Flask, jsonify
from models.db import db
from schemes.ma import ma
from routes.artists import artists_bp
from routes.albums import albums_bp
from routes.users import users_bp
from routes.tracks import tracks_bp
from routes.playlists import playlists_bp
from routes.genres import genres_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/spotify_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(artists_bp)
app.register_blueprint(albums_bp)
app.register_blueprint(users_bp)
app.register_blueprint(tracks_bp)
app.register_blueprint(playlists_bp)
app.register_blueprint(genres_bp)
db.init_app(app)
ma.init_app(app)


@app.route('/ping')
def ping():
    return jsonify({'message': 'pong'})


if __name__ == "__main__":
    app.run(debug=True)
