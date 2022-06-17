from fastapi import FastAPI
from pony.orm import Database
from arc.config import config


app = FastAPI()

db = Database()
db.bind(
    provider=config.provider,
    user=config.user,
    password=config.password,
    host=config.host,
    database=config.database
)
db.generate_mapping(create_tables=True)
