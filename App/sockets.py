from flask_socketio import SocketIO 
from flask_socketio import emit, join_room
from flask import flash

socketio = SocketIO()

def hello_world():
    flash('hello')