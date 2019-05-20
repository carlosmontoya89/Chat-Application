from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):    
    chatroom = session.get('chatroom')
    join_room(chatroom)
    emit('status', {'msg': session.get('name') + ' joined the chatroom.'}, room=chatroom)


@socketio.on('text', namespace='/chat')
def text(message):   
    chatroom = session.get('chatroom')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=chatroom)


@socketio.on('left', namespace='/chat')
def left(message):    
    chatroom = session.get('chatroom')
    leave_room(chatroom)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=chatroom)

