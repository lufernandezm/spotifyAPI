from schemes.ma import ma


class trackSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'uri', 'url', 'href', 'duration_ms', 'popularity', 'album_id')
