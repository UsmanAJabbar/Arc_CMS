from uuid import uuid4
from pony.orm import PrimaryKey, Required, Optional, LongStr
from arc import db
from datetime import datetime
from arc.user.models import User

class Post(db.Entity):
    id = PrimaryKey(uuid4, auto=True)
    created = Required(datetime, default=datetime.now)
    updated = Required(datetime, default=datetime.now)
    title = Required(str)
    content = Optional(LongStr)
    author = Required(User)
