from flask import Flask
from flask_msearch import Search
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

myapp_obj = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
myapp_obj.config.from_mapping(
    SECRET_KEY='you-will-never-guess',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(myapp_obj)
migrate = Migrate(myapp_obj, db)
login_manager = LoginManager(myapp_obj)
login_manager.login_view = 'login'

with myapp_obj.app_context():
    from app.models import *
    db.create_all()

from app import routes