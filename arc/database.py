from pony.orm import Database
from arc.config import config

db = Database()
db.bind(
    provider=config.db_provider,
    user=config.db_user,
    password=config.db_password,
    host=config.db_host,
    database=config.db_database
)
