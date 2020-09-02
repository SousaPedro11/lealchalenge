import os

from dotenv import load_dotenv
from flask_migrate import Migrate

from app import create_app, db

basedir = os.path.abspath(os.path.dirname(__file__))

if os.path.exists(os.path.join(basedir, '.env')):
    load_dotenv(os.path.join(basedir, '.env'))

app = create_app()

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
