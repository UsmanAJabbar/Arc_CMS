from uuid import uuid4, UUID
from pony.orm import PrimaryKey, Required, Optional, LongStr
from arc import db
from datetime import datetime
from arc.user.models import User

class Post(db.Entity):
    id = PrimaryKey(UUID, default=uuid4)
    created = Required(datetime, default=datetime.now)
    updated = Required(datetime, default=datetime.now)
    url = Required(str)

    title = Required(str)
    subtitle = Optional(str)
    content = Optional(LongStr)

    author = Required(User)
    status = Required(int)
