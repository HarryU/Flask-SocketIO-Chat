from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
import random


@socketio.on('joined', namespace='/dm')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/dm')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)


@socketio.on('left', namespace='/dm')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)


@socketio.on('sound', namespace='/dm')
def sound(index):
    room = session.get('room')
    emit('sound', index, room=room)


@socketio.on('add_button', namespace='/dm')
def add_button(button_info):
    room = session.get('room')
    emit('new_button', button_info['name'], room=room)


@socketio.on('dice_roll', namespace='/dm')
def dice_roll(sides, number):
    room = session.get('room')
    result = [random.randint(1, int(sides)) for _ in range(int(number))]
    text({'msg': "You rolled {} on {} {} sided dice.".format(result, number, sides)})
