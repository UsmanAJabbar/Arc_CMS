from fastapi import FastAPI
from pony.orm import Database, db_session
from arc.config import config

app = FastAPI()

db = Database()
db.bind(
    provider=config.db_provider,
    user=config.db_user,
    password=config.db_password,
    host=config.db_host,
    database=config.db_database
)

@app.get('/')
@db_session
def hello_world():
    return {
        'status': 'OK'
    }
