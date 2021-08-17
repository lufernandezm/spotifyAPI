from schemes.ma import ma


class genreSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

