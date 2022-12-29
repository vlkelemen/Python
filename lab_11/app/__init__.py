from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor

from config import config

ckeditor = CKEditor()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'


def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)

    with app.app_context():
        from app.auth import auth_bp
        from app.feedback import feedback_bp
        from app.home import home_bp
        from app.todo import todo_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(feedback_bp)
        app.register_blueprint(home_bp)
        app.register_blueprint(todo_bp)

    return app
