from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from App.sockets import socketio
from flask_socketio import emit, join_room
#from .index import index_views

from App.controllers import (
    createChallenge,
    get_challenges,
    cancel_challenge,
    get_code,
    get_challengeID,
    joinChallenge,
    get_word,
    is_valid
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
        socketio.emit('join_challenge', {'code': code}, room=code)
        return render_template("waiting.html", challenge=challenge)
    else:
        flash('Error Creating Challenge')
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


@challenge_views.route('/join', methods=['POST'])
def join_challenge():
    code = request.form.get('code')
    challenge = joinChallenge(code)
    if challenge:
        flash('Challenge Found')
        socketio.emit('challenge_joined', {'code': code}, room=code)
        #return render_template("game.html", code=code)
        return redirect(url_for('challenge_views.go_to_game', code=code))
    else:
        flash('Invalid code')
        return render_template("index.html")



@challenge_views.route('/game/<string:code>', methods=['GET'])
def go_to_game(code):
    word = get_word()
    return render_template("game.html", code=code, word=word)


@socketio.on('join_challenge')
def handle_join_challenge(data):
    code = data.get('code')
    if is_valid_code(code):  # Ensure you define this function to validate the code
        join_room(code)
        
