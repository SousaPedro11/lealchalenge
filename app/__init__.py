from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

from app.controller.DAO import root_db
from app.controller.cep import cep_bp
from app.controller.challenge import challenge_bp
from app.controller.cpf import cpf_bp
from app.controller.endereco import endereco_bp, db
from config import Config

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app=app)

    db.init_app(app)
    root_db.init_app(app)
    migrate.init_app(app=app, db=db)

    app.register_blueprint(cep_bp)
    app.register_blueprint(challenge_bp)
    app.register_blueprint(cpf_bp)
    app.register_blueprint(endereco_bp)

    with app.app_context():
        db.create_all()

    return app
