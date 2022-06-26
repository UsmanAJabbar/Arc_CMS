from typing import List
from uuid import UUID
import strawberry
from pony.orm import db_session, select, desc

from arc.post.graphql.schema import Post

@strawberry.type
class Query:
    @strawberry.field
    @db_session
    def post(self, id: UUID) -> Post:
        """Takes in an ID and returns the post associated with it

        Raises: ValueError if ID is not found/invalid
        """
        from arc.post.models import Post as PostModel
        from arc.user.models import User as UserModel
        from arc.utils import row_to_dict

        try:
            post = select(
                p for p in PostModel
                if p.id == id
            ).prefetch(UserModel)[:][0]
        except IndexError:
            raise ValueError('Invalid UUID')

        return Post(**row_to_dict(post))

    @strawberry.field
    @db_session
    def posts(self, limit: int = 3, order: str = 'desc') -> List[Post]:
        """Takes in a @limit and @order parameter and returns a list of posts"""
        from arc.post.models import Post as PostModel
        from arc.user.models import User as UserModel
        from arc.utils import row_to_dict

        posts = (
            select(
                p for p in PostModel
                if p.status == 1
            ).prefetch(
                UserModel
            ).order_by(
                desc(PostModel.created) if order == 'desc'
                else PostModel.created
            )
            .limit(limit)
        )[:]

        return [
            Post(**row_to_dict(r))
            for r in posts
        ]

    @strawberry.field
    @db_session
    def post_by_slug(self, slug: str) -> Post:
        """Takes in a slug as a string and returns the post associated with it

        Raises: ValueError if ID is not found/invalid
        """
        from arc.post.models import Post as PostModel
        from arc.user.models import User as UserModel
        from arc.utils import row_to_dict

        try:
            post = select(
                p for p in PostModel
                if p.url == slug
            ).prefetch(UserModel)[:][0]
        except IndexError:
            raise ValueError('Invalid UUID')

        return Post(**row_to_dict(post))


schema = strawberry.Schema(Query)
