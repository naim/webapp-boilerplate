import graphene


class GeoInput(graphene.InputObjectType):
    lat = graphene.Float(required=True)
    lng = graphene.Float(required=True)

    @property
    def latlng(self):
        return "({},{})".format(self.lat, self.lng)


class Address(graphene.ObjectType):
    latlng = graphene.String()
