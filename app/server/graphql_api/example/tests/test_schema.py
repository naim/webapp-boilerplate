import graphene
from graphene.test import Client

from ..queries import Query
from ..mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
client = Client(schema)

query = '''
    query something{
      address(geo: {lat:32.2, lng:12}) {
        latlng
      }
    }
'''

mutation = '''
    mutation addAddress{
      createAddress(geo: {lat:32.2, lng:12}) {
        latlng
      }
    }
'''


def test_query(snapshot):
    snapshot.assert_match(client.execute(query))


def test_mutation(snapshot):
    snapshot.assert_match(client.execute(mutation))
