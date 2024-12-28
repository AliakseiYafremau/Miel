from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    REMOTE_POSTGRES_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    MINUT: int

    API_PREFIX: str = "/api"
    SHOW_DOCS: bool = False


settings = Settings()
