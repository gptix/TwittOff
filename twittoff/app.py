from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Index Page'

    @app.route('/hello')
    def hello():
        return "<h1>Hello, from Mars!</h1>"

    return app
