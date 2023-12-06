from app import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    # Create the database entries for all users with the following data attached to them
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    security_question = db.Column(db.String(128), nullable=False)
    security_answer = db.Column(db.String(128), nullable=False)
    # Establishes a relationship with the 'Note' table which allows access to the user's note
    note = db.relationship('Notes', backref='author', lazy='dynamic')

    # Sets password has based on provided password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    # Checks if provided password matches the stored hashed password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Notes(db.Model):
    # Create the database entries for all notes, this includes the specific ID (queried note), and the remaining data including title/body/timestamp
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=True)
    body_html = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.today().replace(microsecond=0))
    # Incorporate user_id and public to enable/disable note sharing between users and isolate notes from other users (when private)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    public = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Notes {}>'.format(self.body)

