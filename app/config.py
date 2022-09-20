from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    TITLE: str = Field("Squadmakers", env="WEP_APP_TITLE")
    VERSION: str = Field("0.0.0", env="WEB_APP_VERSION")
    DESCRIPTION: str = Field(
        "Service for the manage of the jokes services",
        env="WEP_APP_DESCRIPTION",
    )
    POSTGRES_DATABASE_NAME: str = Field(...)
    POSTGRES_HOST: str = Field(...)
    POSTGRES_PORT: int = Field(...)
    POSTGRES_PASSWORD: str = Field(...)
    POSTGRES_USER: str = Field(...)
    POSTGRES_MINSIZE: str = Field(...)
    POSTGRES_MAXSIZE: str = Field(...)
    DATABASE_URL: str = Field(...)


settings: Settings = Settings()
