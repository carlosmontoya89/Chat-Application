from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import Required, EqualTo


class LoginForm(Form):   
    name = StringField('Name', validators=[Required()])    
    password= PasswordField('PassWord', validators=[Required()])
    submit = SubmitField('Login in')
class RegisterForm(Form):
    name = StringField('Name', validators=[Required()])
    password = PasswordField('PassWord', validators=[Required(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm PassWord', validators=[Required()])
    submit = SubmitField('Register')
class ChatRoomsForm(Form):    
    chatroom = StringField('Room', validators=[Required()])
    submit = SubmitField('Enter to ChatRoom')
