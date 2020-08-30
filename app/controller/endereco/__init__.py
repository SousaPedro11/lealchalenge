from flask import Blueprint

endereco_bp = Blueprint('endereco_bp', __name__)

from . import views
