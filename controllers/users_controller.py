from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt
from models.users import Users
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import create_access_token
from datetime import timedelta
from schemas.users_schema import user_schema


# Default route for all users requests
users = Blueprint('users', __name__, url_prefix='/user')


# Register new users
@users.route('/register', methods=['POST'])
def account_register():
    # Takes in data from the POST
    user_fields = user_schema.load(request.json)
    # Checks to see if the email is already in use.
    user_check = Users.query.filter_by(
        user_email=user_fields["user_email"]).first()
    # Returns an error if the email is already in use.
    if user_check:
        return {"error": "An account has already been created with this email address."}

    # Creates a new user object from entered information.
    user = Users(
        user_name=user_fields["user_name"],
        user_email=user_fields["user_email"],
        user_password=bcrypt.generate_password_hash(
            user_fields["user_password"]).decode("utf-8"),
    )

    # Stages the new user object
    db.session.add(user)
    # Commits the new user object to the database.
    db.session.commit()
    # Generates a token that is set to the user_id value. Good for 30 days
    token = create_access_token(identity=str(
        user.user_id), expires_delta=timedelta(days=30))

    return {"user_name": user.user_name, "token": token}


# Login existing users
@users.route('/login', methods=['POST'])
def account_login():
    # Get username and password
    user_fields = user_schema.load(request.json)
    # Check to see if the username and password exist in the db
    user = Users.query.filter_by(user_email=user_fields["user_email"]).first()

    if not user or not bcrypt.check_password_hash(user.user_password, user_fields["user_password"]):
        return abort(401, description="Invalid Username or Password")

    # Generates a token that is set to the user_id value. Good for 30 days
    access_token = create_access_token(identity=str(
        user.user_id), expires_delta=timedelta(days=30))

    return jsonify({"user": user.user_name, "token": access_token})


# Validation error messages
@users.errorhandler(ValidationError)
def register_validation_error(error):

    return error.messages, 400
