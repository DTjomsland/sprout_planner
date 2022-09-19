from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.users import Users
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length

users = Blueprint('users', __name__, url_prefix='/users')

class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'user_email', 'user_password', 'admin')
    password = ma.String(validate=Length(min=8))

user_schema = UserSchema()
users_schema = UserSchema(many=True)