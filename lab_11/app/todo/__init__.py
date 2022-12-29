from flask import Blueprint

todo_bp = Blueprint('todo', __name__, url_prefix='/task', template_folder='templates/todo')

from . import views
