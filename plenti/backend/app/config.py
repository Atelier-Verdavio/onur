from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    MQTT_BROKER: str
    MQTT_PORT: int
    MQTT_USERNAME: str
    MQTT_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings() 