from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.icon import Icon
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length
from schemas.icon_schema import icon_schema, icons_schema

# Default route for all icon requests
icon = Blueprint('icon', __name__, url_prefix='/icon')