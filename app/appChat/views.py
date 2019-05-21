from flask import session, redirect, url_for, render_template, request, flash
from . import main
from .forms import LoginForm, RegisterForm, ChatRoomsForm
from .models import UserModel, Message
from werkzeug.security import safe_str_cmp
from app import login_required


@main.route('/', methods=['GET', 'POST'])
def login():
    """Login form to enter a room."""
    error=""
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        user = UserModel.find_by_username(name)
        if user and safe_str_cmp(user.password, password):
            session['logged_in'] = True
            session['name'] = name
            session['id']=user.id
            print(session['id'])
            return redirect(url_for('.chatroom'))
        else:
            flash( "Invalid credentials, try again.")
    elif request.method == 'GET':
        form.name.data = session.get('name', '')        
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
        session['id']=user.id        
        flash("User created successfully.")
        return redirect(url_for('.chatroom'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')        
    return render_template('register.html',form=form)

@main.route('/chatroom/', methods=['GET', 'POST'])
@login_required
def chatroom():
    form = ChatRoomsForm() 
    if form.validate_on_submit():
        session['chatroom'] = form.chatroom.data
        return redirect(url_for('.chat'))    
    return render_template('chatroom.html', form=form)


@main.route('/chat')
@login_required
def chat():   
    name = session.get('name', '')
    chatroom = session.get('chatroom', '')
    if name == '' or chatroom == '':
        return redirect(url_for('.login'))
    return render_template('chat.html', name=name, chatroom=chatroom)

@main.route('/messages/')
@login_required
def messages():
    name = session.get('name', '')
    chatroom = session.get('chatroom', '')   
    messages=Message.find_by_name_id(session.get('id')) 
    messages=messages[0:49]   
    return render_template('messages.html', messages=messages, name=name, chatroom=chatroom)


@main.route('/logout/')
@login_required
def logout():   
    session.clear()
    flash("You have been logged out!")    
    return redirect(url_for('.login'))
    
