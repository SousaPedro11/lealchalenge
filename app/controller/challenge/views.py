from flask import render_template

from app.controller.challenge import challenge_bp


@challenge_bp.route('/')
def home():
    return render_template('home.html')


@challenge_bp.route('/tsql/')
def tsql():
    return render_template('tsql.html')


@challenge_bp.route('/viacep/')
def viacep():
    return render_template('viacep.html')
