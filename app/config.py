from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    TITLE: str = Field("Thori Redis-DB", env="WEP_APP_TITLE")
    VERSION: str = Field("0.0.0", env="WEB_APP_VERSION")
    DESCRIPTION: str = Field(
        "Micro service for the manage of the redis-db services",
        env="WEP_APP_DESCRIPTION",
    )
    POSTGRES_DATABASE_NAME: str = Field(...)
    POSTGRES_HOST: str = Field(...)
    POSTGRES_PORT: int = Field(...)
    POSTGRES_PASSWORD: str = Field(...)
    POSTGRES_USER: str = Field(...)
    POSTGRES_MINSIZE: str = Field(...)
    POSTGRES_MAXSIZE: str = Field(...)


settings: Settings = Settings()
