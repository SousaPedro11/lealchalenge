from flask import Blueprint

cpf_bp = Blueprint('cpf_bp', __name__)

from . import views
