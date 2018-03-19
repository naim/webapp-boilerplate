import graphene

from .types import GeoInput, Address


class CreateAddress(graphene.Mutation):

    class Arguments:
        geo = GeoInput(required=True)

    Output = Address

    def mutate(self, info, geo):
        return Address(latlng=geo.latlng)


class Mutation(graphene.ObjectType):
    create_address = CreateAddress.Field()
