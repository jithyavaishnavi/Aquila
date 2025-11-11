from flask import Blueprint
from .route import main  # import your blueprint

def register_routes(app):
    app.register_blueprint(main)
