from dotenv import load_dotenv
from decouple import config
from flask import Flask, render_template, request

from .models import DB, User
from .twitter import add_or_update_user

load_dotenv()

  
def create_app():
    """Create, configure an instance of the Flask application"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    DB.init_app(app)

    @app.route('/')
    def root():
        DB.create_all()
        return render_template(
            'base.html', title='Thorium Incorporated!', users=User.query.all())


    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None, message=''):
        name = name or request.values['username']
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message = f'User {name} successfully updated!'.tweets
        except Exception as e:
            message = f'Error while trying to add user {name}: {e}'
            tweets = []
        return render_template('user.html', title=name, message=message, tweets=tweets)




    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='RESET THE KRAKEN!')

    return app


def add_user(username):
    # get twitter user data from tweepy API
    twitter_user = TWITTER.get_user(username)

    # Add user unfo to User table in database
    db_user = User(id=twitter_user.id, username=twitter_user.name)
    DB.session.add(db_user)

    
