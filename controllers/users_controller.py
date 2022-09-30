from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.users import Users
from models.user_activity import UserActivity
from flask_jwt_extended import  create_access_token
from datetime import timedelta
from schemas.users_schema import user_schema, users_schema
from schemas.user_activity_schema import UserActivitySchema
from sqlalchemy import select, join


# Default route for all users requests
users = Blueprint('users', __name__, url_prefix='/user')



# Register new users
@users.route('/register', methods=['POST'])
def account_register():
    # Takes in data from the POST
    user_fields = user_schema.load(request.json)
    # Checks to see if the email is already in use.
    user = Users.query.filter_by(user_email = user_fields["user_email"]).first()
    # Returns an error if the email is already in use.
    if user:
        return {"error": "An account has already been created with this email address."}
    
    # Creates a new user object from entered information.
    user = Users(
        user_name = user_fields["user_name"],
        user_email = user_fields["user_email"],
        user_password = bcrypt.generate_password_hash(user_fields["user_password"]).decode("utf-8"),
   )

    # Stages the new user object
    db.session.add(user)
    # Commits the new user object to the database.
    db.session.commit()

    token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=30)) 
    
    return {"user_name": user.user_name, "token": token}
    

# Login existing users
@users.route('/login', methods=['POST'])
def account_login():

    user_fields = user_schema.load(request.json)

    user = Users.query.filter_by(user_email=user_fields["user_email"]).first()

    if not user or not bcrypt.check_password_hash(user.user_password, user_fields["user_password"]):
        return abort(401, description = "Invalid Username or Password")
    
    # Return the access token with the user_name(For Display Use)
    access_token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
    return jsonify({"user": user.user_name, "token": access_token})