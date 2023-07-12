from flask import Flask
from database import setup_db
import database.models as models
from marshmallow import ValidationError


def create_app(config='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config)

    setup_db(app)

    # ROUTES
    @app.get("/")
    def index():
        return {"message": "Hello World"}

    # ERROR HANDLERS
    @app.errorhandler(ValidationError)
    def handle_marshmallow_validation(err):
        return {'errors': err.messages, 'message': 'invalid data'}, 400

    return app
