from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

endereco_bp = Blueprint('endereco_bp', __name__)

db = SQLAlchemy()

from . import views
