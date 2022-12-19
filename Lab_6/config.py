import os
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = 'supersecretkey'
WTF_CSRF_ENABLED = True
# Database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'site.db')
