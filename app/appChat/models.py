from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime)  
    name_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    origin = db.relationship('UserModel')
    

    def __init__(self, content, created_at, name_id):
        self.content = content
        self.created_at =created_at
        self.name_id = name_id

    class Meta:
        ordering = ['-created_at']