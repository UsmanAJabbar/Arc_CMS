from pydantic import BaseSettings


class Config(BaseSettings):
    db_provider: str
    db_host: str
    db_user: str
    db_password: str
    db_database: str

    class Config:
        env_file = '.env'

config = Config()
