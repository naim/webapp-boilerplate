import graphene

from .types import GeoInput, Address


class Query(graphene.ObjectType):
    address = graphene.Field(Address, geo=GeoInput(required=True))

    def resolve_address(self, info, geo):
        return Address(latlng=geo.latlng)
