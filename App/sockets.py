from flask_socketio import SocketIO 
from flask import flash

socketio = SocketIO()

def hello_world():
    flash('hello')