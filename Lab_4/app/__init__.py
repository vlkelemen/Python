from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

from app import routes
