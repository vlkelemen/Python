from os import environ

from app import create_app

if __name__ == '__main__':
    app = create_app(environ.get('FLASK_CONFIG'))
    app.run()
