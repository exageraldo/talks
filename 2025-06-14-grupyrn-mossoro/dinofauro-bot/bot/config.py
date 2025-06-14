from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    bot_key: str

settings = Settings()