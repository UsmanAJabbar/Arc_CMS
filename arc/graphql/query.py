import strawberry
from strawberry.tools import merge_types as merge_schemas

from arc.post.graphql.query import PostQueries

Query = merge_schemas(
    'Query',
    (PostQueries,)
)

schema = strawberry.Schema(Query)
