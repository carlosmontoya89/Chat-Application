from flask import session, redirect, url_for, render_template, request, flash
from . import main
from .forms import LoginForm, RegisterForm
from .models import UserModel
from werkzeug.security import safe_str_cmp



@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.chatroom.data
        user = UserModel.find_by_username(name)
        if user and safe_str_cmp(user.password, password):
            session['logged_in'] = True
            session['name'] = name
        return redirect(url_for('.chat'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.chatroom.data = session.get('chatroom', '')
    return render_template('index.html', form=form)

@main.route('/login/', methods=['GET', 'POST'])
def login():
    """Login form to enter a room."""
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.chatroom.data
        user = UserModel.find_by_username(name)
        if user and safe_str_cmp(user.password, password):
            session['logged_in'] = True
            session['name'] = name
            return redirect(url_for('.chat'))
        else:
            error = "Invalid credentials, try again."
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.chatroom.data = session.get('chatroom', '')
    return render_template('login.html', form=form, error=error)

@main.route('/register/', methods=['GET', 'POST'])
def register():
    """Register form to enter a room."""
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        if UserModel.find_by_username(name):
            flash("A user with that username already exists")
            return render_template('register.html',form=form)
        user = UserModel(name, password)
        user.save_to_db()
        session['logged_in'] = True
        session['name'] = name
        flash("User created successfully.")
        return redirect(url_for('.index'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.password.data = session.get('chatroom', '')
    return render_template('register.html',form=form)


@main.route('/chat')
def chat():   
    name = session.get('name', '')
    chatroom = session.get('chatroom', '')
    if name == '' or chatroom == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=chatroom)
