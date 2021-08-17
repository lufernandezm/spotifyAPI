from schemes.ma import ma


class albumSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'uri', 'url', 'href', 'total_tracks', 'popularity', 'img', 'label', 'release_date')
