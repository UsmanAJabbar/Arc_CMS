import strawberry

from datetime import datetime
from uuid import UUID

@strawberry.type
class User:
    id: UUID
    created: datetime
    updated: datetime

    name: str
    username: str
    email: str
    password: str

    active: bool
    role: int
