import os


class Config:
    THREADED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
    # 'storage.db')
    DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DATABASE_URI}'
