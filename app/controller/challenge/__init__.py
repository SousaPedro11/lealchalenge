from flask import Blueprint

challenge_bp = Blueprint('challenge_bp', __name__)

from . import views
