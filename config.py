import os

class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "chave-super-segura"
    )

    SQLALCHEMY_DATABASE_URI = "sqlite:///academia.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False