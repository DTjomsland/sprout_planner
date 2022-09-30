from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# from datetime import timedelta
from flask_marshmallow import Marshmallow
# from marshmallow.validate import Length
# import psycopg2
# import config
from flask_bcrypt import Bcrypt
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required


db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()

def create_app():

    app = Flask(__name__)

    app.config.from_object("config.app_config")

    db.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    return app