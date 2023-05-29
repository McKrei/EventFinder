from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config.from_object('config.Config')

db = SQLAlchemy(app)

from .database import models, crud
from . import views

db.create_all()
