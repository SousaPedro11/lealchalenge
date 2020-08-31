from os import urandom


class Config:
    SECRET_KEY = urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    THREADED = True
