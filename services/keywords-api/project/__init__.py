# services/users/project/__init__.py


import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# instantiate the extensions
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app_settings='project.config.DevelopmentConfig'
    #print(os.environ)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
    app.debug = False
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # register blueprints
    from project.api.keyword import keywords_blueprint
    app.register_blueprint(keywords_blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app, 'db': db})
    return app
