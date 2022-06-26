import strawberry
from pony.orm import db_session, select
from arc.post.graphql.schema import Post
from uuid import UUID


@strawberry.type
class Query:

    @strawberry.field
    @db_session
    def get_post(self, id: UUID) -> Post:
        from arc.post.models import Post as PostModel
        from arc.user.models import User as UserModel

        try:
            post = select(
                p for p in PostModel
                if p.id == id
            ).prefetch(UserModel)[:][0]
        except IndexError:
            raise ValueError('Invalid UUID')

        post_details = {
            c: getattr(post, c)
            for c in post._columns_
        }

        return Post(**post_details)


schema = strawberry.Schema(Query)
