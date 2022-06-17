from uuid import uuid4
from pony.orm import PrimaryKey, Required, Optional, LongStr
from datetime import datetime
from arc import db


class User(db.Entity):
    id = PrimaryKey(uuid4, auto=True)
    created = Required(datetime, default=datetime.now)
    updated = Required(datetime, default=datetime.now)
    username = Required(str)
    password = Required(str)
    email = Required(str)
    active = Required(bool)
    role = Required(bool)
