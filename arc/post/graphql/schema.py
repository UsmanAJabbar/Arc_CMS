import strawberry
from datetime import datetime
from uuid import UUID
from pony.orm import db_session

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

    # @db_session
    # @strawberry.field
    # def author(self) -> User:
    #     print('=======================')
    #     print('=======================')
    #     print('=======================')
    #     print('=======================')
    #     from arc.user.models import User as UserModel
    #     return User(**self)
