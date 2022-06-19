from flask import Flask
try:
    from flask_restplus import Api
except ImportError:
    import werkzeug
    werkzeug.cached_property = werkzeug.utils.cached_property
    from flask_restplus import Api
from app.routes import setup_routes


def create_app():
    flask = Flask(__name__)
    app = Api(app=flask)
    setup_routes(app)
    return flask


def run():
    flask = create_app()
    flask.run()

if __name__ == "__main__":
    create_app()
