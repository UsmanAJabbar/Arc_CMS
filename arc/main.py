from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from fastapi.middleware.cors import CORSMiddleware
from arc.graphql.query import schema

app = FastAPI()

# Allows OPTIONS pre-flight requests from browsers to come in
app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_origins=["*"],
    allow_methods=["*"]
)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix='/graphql')

@app.get('/')
def status():
    return {
        'status': 'OK'
    }
