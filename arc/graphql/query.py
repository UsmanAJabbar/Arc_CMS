import strawberry
from strawberry.tools import merge_types as merge_schemas

from arc.post.graphql.query import PostQueries
from arc.user.graphql.query import UserQueries

Query = merge_schemas(
    'Query',
    (
        PostQueries,
        UserQueries,
    )
)

schema = strawberry.Schema(Query)
