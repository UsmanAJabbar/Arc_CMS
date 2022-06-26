from arc.main import (
    app,
    db,
)

from arc.post.models import Post
from arc.user.models import User

db.generate_mapping(create_tables=True)
