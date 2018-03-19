from graphene import Schema

import graphql_api.query as query
import graphql_api.mutation as mutation

schema = Schema(query=query.Queries, mutation=mutation.Mutations)
