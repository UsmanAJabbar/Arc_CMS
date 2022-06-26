from arc.main import app
from arc.database import db

db.generate_mapping(create_tables=True)
