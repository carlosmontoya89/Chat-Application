from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):   
    name = StringField('Name', validators=[Required()])
    chatroom = StringField('Room', validators=[Required()])
    #password= PasswordField('PassWord', validators=[Required()])
    submit = SubmitField('Enter Chatroom')
