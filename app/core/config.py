from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Crop Price Prediction API"
    DATABASE_URL: str = "mysql+pymysql://root:@localhost:3306/smartkrishi_admin"
    SECRET_KEY: str = "YOUR_SECRET_KEY"  # To be updated later
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
