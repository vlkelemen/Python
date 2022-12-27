from flask import Blueprint

todo_bp = Blueprint('todo', __name__, url_prefix='/task')

from . import views
