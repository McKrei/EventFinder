from flask import render_template, redirect, url_for

from . import app, db
from .database import models


@app.route('/')
def index():
    return render_template('index.html',
                           title='Главная')
