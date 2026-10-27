from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")
    database_url: str = "sqlite+aiosqlite:///./bank.db"
    environment: str = "production"
    jwt_secret_key: str = "supersecretkey"
    jwt_algorithm: str = "HS256"

settings = Settings()
