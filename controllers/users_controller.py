from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.users import Users
from flask_jwt_extended import  create_access_token
from datetime import timedelta
from schemas.users_schema import user_schema, users_schema


# Default route for all users requests
users = Blueprint('users', __name__, url_prefix='/users')


@users.route('/register', methods=['POST'])
def account_register():
   
    user_fields = user_schema.load(request.json)
    print(user_fields["user_email"])
    print(user_fields["user_password"])

    user = Users(
        user_email = user_fields["user_email"],
        user_password = bcrypt.generate_password_hash(user_fields["user_password"]).decode("utf-8"),
   )

    db.session.add(user)

    db.session.commit()
    return jsonify((user_schema).dump(user))
    
@users.route('/login', methods=['POST'])
def account_login():

    user_fields = user_schema.load(request.json)

    user = Users.query.filter_by(user_email=user_fields["user_email"]).first()

    if not user or not bcrypt.check_password_hash(user.user_password, user_fields["user_password"]):
        return abort(401, description = "Invalid Username or Password")
    
    access_token = create_access_token(identity=str(user.user_id), expires_delta=timedelta(days=1))
    return jsonify({"user": user.user_email, "token": access_token})