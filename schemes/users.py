from schemes.ma import ma


class userSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'uri', 'url', 'href', 'followers', 'img')

