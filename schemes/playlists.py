from schemes.ma import ma


class playlistSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'uri', 'url', 'href', 'description', 'followers', 'img', 'user_id')
