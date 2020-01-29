from flask import Flask, render_template
from .models import DB

def create_app():
    """Create and configure an instance of the Flask app.."""

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init.app(app)    

    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return render_template('base.html', title='Howdy', users=User.query.all())
    
    return app

