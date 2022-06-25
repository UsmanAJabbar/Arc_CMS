import strawberry
from datetime import datetime
from uuid import UUID

from arc.user.graphql.schema import User


@strawberry.type
class Post:
    id: UUID
    created: datetime
    updated: datetime
    url: str

    title: str
    subtitle: str
    content: str

    status: int

    author: User
