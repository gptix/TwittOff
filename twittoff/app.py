from dotenv import load_dotenv
from decouple import config
from flask import Flask, render_template

from .models import DB, User

load_dotenv()


def create_app():
    """Create and configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        DB.create_all()
        return render_template(
            'base.html', title='Thorium Incorporated!', users=User.query.all())

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='RESET THE KRAKEN!')

#    @app.route('/user', methods='POST')

    # @app.route('/user/<name>', methods='GET')
    # def user(name=name, message=""):
    #     name = name or request.values['user name']:
    #     try:
    #         if request.method = 'POST':
    #             add_or_update_user(name)
    #             message = f'User {name} successfully added!'
    #             tweets = User.query.filter{User.name == ).one().tweets

    return app
