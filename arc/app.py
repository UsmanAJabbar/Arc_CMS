from fastapi import FastAPI
from pony.orm import Database
from strawberry.fastapi import GraphQLRouter

from arc.config import config
from arc.graphql.query import schema


app = FastAPI()

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix='/graphql')

db = Database()
db.bind(
    provider=config.db_provider,
    user=config.db_user,
    password=config.db_password,
    host=config.db_host,
    database=config.db_database
)


@app.get('/')
def status():
    return { 'status': 'OK' }
