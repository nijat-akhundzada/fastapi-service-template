from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    service_name: str = "service"
    env: str = "local"
    log_level: str = "INFO"
    database_url: str


settings = Settings()
