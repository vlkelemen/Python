import os

basedir = os.path.abspath(os.path.dirname(__file__))

# General config
WTF_CSRF_ENABLED = True
SECRET_KEY = 'ENCRYPTED_KEY'

# Database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'site.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False
