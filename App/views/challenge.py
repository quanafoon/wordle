from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from .index import index_views

from App.controllers import (
    createChallenge,
    get_challenges,
    cancel_challenge,
    get_code,
    get_challengeID,
)

challenge_views = Blueprint('challenge_views', __name__, template_folder='../templates')

@challenge_views.route('/create', methods=['GET'])
def display():
    return render_template("create.html")


@challenge_views.route('/waiting', methods=['POST'])
def create_challenge():
    code = request.form.get('code')
    challenge = createChallenge(code)
    if challenge:
        flash('Challenge Created')
        return render_template("waiting.html", code=code)
    else:
        flash('almost!')
        return render_template("index.html")


@challenge_views.route('/challenges', methods=['GET'])
def challenge_list():
    challenges = get_challenges()
    return jsonify(challenges)


@challenge_views.route('/cancel/<string:code>', methods=['POST'])
def cancel_challenge_route(code):
    challenge_id = get_challengeID(code)
    if challenge_id:
        challenge = cancel_challenge(challenge_id)
        if challenge:
            flash('Challenge Cancelled')
            return render_template("index.html")
        else:
            flash('Error in canceling the challenge.')
            return render_template("waiting.html", code=code)
    else:
        flash('Challenge not found.')
        return render_template("waiting.html", code=code)