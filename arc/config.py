from pydantic import BaseSettings


class Config(BaseSettings):
    provider: str
    host: str
    user: str
    password: str
    database: str
    port: int

    class Config:
        env_file = '.env'

config = Config()
