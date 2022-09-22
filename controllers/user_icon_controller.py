from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.user_icon import UserIcon
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length
from schemas.user_icon_schema import user_icon_schema, user_icons_schema

# Default route for all user icon requests
user_icon = Blueprint('user_icon', __name__, url_prefix='/usericon')

