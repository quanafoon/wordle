from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    generateID
)

challenge_views = Blueprint('challenge_views', __name__, template_folder='../templates')

@challenge_views.route('/waiting', methods=['GET'])
def create_challenge():
    challengeID = generateID()
    flash('almost!')
    return render_template("waiting.html")

