from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.user_activity import UserActivity
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length
from schemas.user_activity_schema import user_activity_schema, user_activities_schema

# Default route for all user activity requests
user_activity = Blueprint('user_activity', __name__, url_prefix='/useractivity')