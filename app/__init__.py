from flask import Flask, session, redirect, url_for, render_template, request, flash
from flask_socketio import SocketIO
from functools import wraps

socketio = SocketIO()

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('.login'))

    return wrap
		

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .appChat import main as main_blueprint
    app.register_blueprint(main_blueprint)

    socketio.init_app(app)    
    return app

