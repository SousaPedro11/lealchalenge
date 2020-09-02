import os


class Config:
    THREADED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
    # 'storage.db')

    HOST = os.environ.get('DB_HOST')
    DATABASE = os.environ.get('DB_DATABASE')
    USER = os.environ.get('DB_USER')
    PORT = os.environ.get('DB_PORT')
    PASS = os.environ.get('DB_PASS')
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USER}:{PASS}@{HOST}:{PORT}/{DATABASE}'
