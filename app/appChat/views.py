from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['chatroom'] = form.chatroom.data
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.chatroom.data = session.get('chatroom', '')
    return render_template('index.html', form=form)


@main.route('/chat')
def chat():   
    name = session.get('name', '')
    chatroom = session.get('chatroom', '')
    if name == '' or chatroom == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=chatroom)
