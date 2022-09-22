from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.icon import Icon
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length
from schemas.icon_schema import icon_schema, icons_schema

# Default route for all icon requests
icon = Blueprint('icon', __name__, url_prefix='/icon')

# Get request for all pre-designed icons
@icon.route('/', methods=['GET'])
def get_icons():
    icons = Icon.query.all()
    result = icons_schema.dump(icons)
    return jsonify(result)

# Get request for a single pre-designed icon
@icon.route('/<int:icon_id>', methods=['GET'])
def get_icon(icon_id):
    icon = Icon.query.get(icon_id)
    result = icon_schema.dump(icon)
    return jsonify(result)