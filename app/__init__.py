from flask import Flask
from .extensions import db
from flask_migrate import Migrate
from .models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    return app
