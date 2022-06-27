from typing import List
from uuid import UUID
import strawberry
from pony.orm import db_session, select

from arc.user.graphql.schema import User
from arc.user.models import User as UserModel
from arc.utils import row_to_dict


@strawberry.type
class UserQueries:
    @strawberry.field
    @db_session
    def user(self, id: UUID) -> User:
        try:
            user = UserModel[id]
        except IndexError:
            raise ValueError('Invalid UUID')

        return User(**row_to_dict(user))

    @strawberry.field
    @db_session
    def users(self) -> List[User]:        
        users = select(u for u in UserModel)

        return [
            User(**row_to_dict(u))
            for u in users
        ]
