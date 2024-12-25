from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    DB_HOST: str
    DB_PORT: str
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    REMOTE_POSTGRES_URL: str

    SECRET_KEY: str
    ALGORITHM: str
    MINUT: int


settings = Settings()
