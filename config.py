# config.py
class Config:
    SECRET_KEY = "your-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///aquila.db"  # SQLite DB in project root
    SQLALCHEMY_TRACK_MODIFICATIONS = False
