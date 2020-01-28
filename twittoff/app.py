from flask import Flask
from .models import DB

#Linux
#'sqlite:////absolute/path/to/db.sqlite3'


def create_app():
    """Create and configure an instance of the Flask app.."""

    app = Flask(__name__)
#    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///absolute path from above'
#    DB.init.app(app)
    

    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return "<h1>Hello, from Mars!</h1>"

    return app
