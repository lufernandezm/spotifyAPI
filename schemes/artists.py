from schemes.ma import ma


class artistSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'uri', 'url', 'href', 'followers', 'popularity', 'img')

