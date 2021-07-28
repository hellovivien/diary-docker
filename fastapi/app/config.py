import secrets
from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Diary"
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///app/diary.db?check_same_thread=False"
    SECRET_KEY: str = 'test'
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    MONITORING_ACTIVE: bool =  True

#     class Config:
#         case_sensitive = True


settings = Settings()
