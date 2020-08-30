from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from app.controller.challenge import challenge_bp
from app.controller.cpf import cpf_bp
from app.controller.cep import cep_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app=app)
db = SQLAlchemy(app=app)

app.register_blueprint(cep_bp)
app.register_blueprint(challenge_bp)
app.register_blueprint(cpf_bp)
