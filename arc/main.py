from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from arc.graphql.query import schema

app = FastAPI()

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix='/graphql')

@app.get('/')
def status():
    return { 'status': 'OK' }
