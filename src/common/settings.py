from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str

    class Config:
        env_file = ".env"


class DatabaseSettings(BaseSettings):
    postgres_url: str = None

    @classmethod
    def generate(cls):
        generic_settings = Settings()
        postgres_url = "postgresql://"+generic_settings.postgres_user+":"+generic_settings.postgres_password+"@localhost/"+generic_settings.postgres_db
        return cls(postgres_url=postgres_url)

    class Config:
        env_file = ".env"


@lru_cache
def get_databse_settings() -> DatabaseSettings:
    return DatabaseSettings().generate()
