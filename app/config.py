from os import environ

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


class Config:
    FLASK_DEBUG = environ.get("FLASK_DEBUG")

    POSTGRES_HOST = environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_PORT = environ.get("POSTGRES_PORT", "5432")
    POSTGRES_USER = environ.get("POSTGRES_USER", "user")
    POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD", "password")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/test-flask-app"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


settings = Config
