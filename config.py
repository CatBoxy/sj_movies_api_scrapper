from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "sj_movies_api"

    class Config:
        env_file = ".env"
