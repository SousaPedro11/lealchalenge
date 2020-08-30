from flask import Blueprint

cep_bp = Blueprint('cep_bp', __name__)

from . import views
