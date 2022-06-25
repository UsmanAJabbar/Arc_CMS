import strawberry
from typing import List
from pony.orm import db_session, select
from arc.post.graphql.schema import Post
from uuid import UUID


@strawberry.type
class Query:

    @strawberry.field
    @db_session
    def get_post(self, id: UUID) -> Post:
        from arc.post.models import Post as PostModel
        post = PostModel.get(id=id)
        columns = post._columns_

        return Post(**{
            c_name: getattr(post, c_name)
            for c_name in columns
        })


schema = strawberry.Schema(Query)
