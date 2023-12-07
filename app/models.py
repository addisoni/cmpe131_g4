from app import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    # Creates the database entries for all users with the following data attached to them
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    security_question = db.Column(db.String(128), nullable=False)
    security_answer = db.Column(db.String(128), nullable=False)

    # Establishes a bidirectional relationship
    notes = db.relationship('Notes', back_populates='author', lazy='dynamic')
    folders = db.relationship('Folder', back_populates='user', lazy='dynamic')

    # Sets password has based on provided password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    # Checks if provided password matches the stored hashed password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Notes(db.Model):
    # Creates the database entries for all notes, this includes the specific ID (queried note), and the reamining data including title/body/date_created
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=True)
    old_body = db.Column(db.Text, nullable=True)

    date_created = db.Column(db.DateTime, index=True, default=datetime.today().replace(microsecond=0))
    last_modified = db.Column(db.String, index=True)

    # Create user_id, folder_id, and public to enable/disable note sharing between users and isolate notes from other users (when private)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))
    public = db.Column(db.Boolean, default=False)

    # Establish bidirectional relationship
    author = db.relationship('User', back_populates='notes')
    folder = db.relationship('Folder', back_populates='notes')

    def __repr__(self):
        return '<Notes {}>'.format(self.body)

class Folder(db.Model):
    # Creates the database entries for all folders
    id = db.Column(db.Integer, primary_key=True)
    folder_name = db.Column(db.String(64), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Establish bidirectional relationship
    user = db.relationship('User', back_populates='folders')
    notes = db.relationship('Notes', back_populates='folder', lazy='dynamic', foreign_keys='Notes.folder_id')

    def __repr__(self):
        return '<Folder {}>'.format(self.folder_name)