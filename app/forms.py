from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo
from markupsafe import Markup
from wtforms.fields import TextAreaField, HiddenField

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class CreateAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message = 'Passwords must match')])
    confirm = PasswordField('Repeat Password')
    security_question = SelectField('Security Question', choices=[
        ('q1', 'What city were you born in?'),
        ('q2', 'What was your childhood nickname?'),
        ('q3', 'What was the name of your first childhood friend?'),
        ('q4', 'Who is your most memorable teacher?'),
        ('q5', 'What was the name of your first pet?')],
        validators=[DataRequired()])
    security_answer = StringField('Security Answer', validators=[DataRequired()])
    
    submit = SubmitField('Create Account')

class NoteForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', render_kw={'class': 'editor'})  # Add this line
    submit = SubmitField('Submit')
    action = HiddenField()
    
class ModifyAccountForm(FlaskForm):
    username = StringField('New Username')
    password = PasswordField('New Password', validators=[EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat New Password')
    security_question = SelectField('New Security Question', choices=[
        ('q1', 'What city were you born in?'),
        ('q2', 'What was your childhood nickname?'),
        ('q3', 'What was the name of your first childhood friend?'),
        ('q4', 'Who is your most memorable teacher?'),
        ('q5', 'What was the name of your first pet?')])
    security_answer = StringField('New Security Answer')
    submit = SubmitField('Modify Account')
