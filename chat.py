#!/bin/env python
from app import create_app, socketio

app = create_app(debug=True)
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    socketio.run(app)
