from uuid import UUID, uuid4
from pony.orm import PrimaryKey, Required, Set
from datetime import datetime

from arc import db


class User(db.Entity):
    id = PrimaryKey(UUID, default=uuid4)
    created = Required(datetime, default=datetime.now)
    updated = Required(datetime, default=datetime.now)

    name = Required(str)
    username = Required(str)
    email = Required(str)
    password = Required(str)

    active = Required(bool)
    role = Required(int)

    posts = Set('Post')
