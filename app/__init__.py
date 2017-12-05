# app package constructor imports most extensions
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

# then creates them uninitialized (no app as arg)
bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    """ Application factory with selected config name as argument """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # Run config specific configurations (if any)
    config[config_name].init_app(app)
    # Initialize extensions with new app instance
    bootstrap.init_app(app)
    db.init_app(app)

    # Attach routes and custom error pages
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    # Factory function returns app instance
    return app
