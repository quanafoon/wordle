from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    load_words,
    get_words
)

words_views = Blueprint('words_views', __name__, template_folder='../templates')

@words_views.route('/words', methods=['GET'])
def word_list():
    words = get_words()
    return jsonify(words)