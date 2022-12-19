# -*- coding: UTF-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

from app import views, models
