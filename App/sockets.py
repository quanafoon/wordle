from flask_socketio import SocketIO 
from flask_socketio import emit, join_room

socketio = SocketIO()

@socketio.on('join_challenge')
def handle_join_challenge(data):
    code = data['code']
    join_room(code)
    emit('challenge_joined', {'code': code}, room=code)

def hello_world():
    flash('hello')