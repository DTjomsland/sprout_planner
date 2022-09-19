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




# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://david:Cygyxy64rtfg@localhost:5432/sprout_planner"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['JWT_SECRET_KEY'] = "This is a secret"

#db = SQLAlchemy(app)
# ma = Marshmallow(app)
# bcrypt = Bcrypt(app)
# jwt = JWTManager(app)


# class UserSchema(ma.Schema):
#     class Meta:
#         fields = ('user_id', 'user_email', 'user_password', 'admin')
#     password = ma.String(validate=Length(min=8))

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

# # User table creation
# class Users(db.Model):
#     __tablename__="users"
    
#     # User columns
#     user_id = db.Column(db.Integer, primary_key=True)
#     user_email = db.Column(db.String, unique=True, nullable=False)
#     user_password = db.Column(db.String(60), nullable=False)
#     admin = db.Column(db.Boolean, default=False)

# #Create the database tables
# @app.cli.command('create')
# def create_db():
#     db.create_all()
#     print("Creating tables...")

# @app.cli.command('drop')
# def drop_db():
#     db.drop_all()
#     print("Dropping tables...")

# # Seeding the database
# @app.cli.command('seed')
# def seed_db():
#     users = Users(
#         user_email = "user@gmail.com",
#         user_password = bcrypt.generate_password_hash("password").decode("utf-8"),
#     )

#     db.session.add(users)

#     admin = Users(
#         user_email = "admin@gmail.com",
#         user_password = bcrypt.generate_password_hash("password").decode("utf-8"),
#         admin = True
#     )

#     db.session.add(admin)

#     db.session.commit()
#     print("Seeding tables...")

# @app.route('/')
# @jwt_required()
# def welcome():
#     return "Sprout Planner under construction"

# @app.route('/auth/register', methods=['POST'])
# def auth_register():
   
#     user_fields = user_schema.load(request.json)
#     print(user_fields["user_email"])
#     print(user_fields["user_password"])

#     user = Users(
#         user_email = user_fields["user_email"],
#         user_password = bcrypt.generate_password_hash(user_fields["user_password"]).decode("utf-8"),
#    )

#     db.session.add(user)

#     db.session.commit()
#     return jsonify((user_schema).dump(user))

# @app.route('/auth/login', methods=['POST'])
# def auth_login():

#     user_fields = user_schema.load(request.json)

#     user = Users.query.filter_by(user_email=user_fields["user_email"]).first()

#     if not user or not bcrypt.check_password_hash(user.user_password, user_fields["user_password"]):
#         return abort(401, description = "Invalid Username or Password")
    
#     access_token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
#     return jsonify({"user": user.user_email, "token": access_token})

# if __name__ == '__main__':
#     app.run(debug=True)