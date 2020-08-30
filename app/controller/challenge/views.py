from flask import render_template

from app.controller.challenge import challenge_bp


@challenge_bp.route('/')
def home():
    return render_template('home.html')
