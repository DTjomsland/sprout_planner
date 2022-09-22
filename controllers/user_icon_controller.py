from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.user_icon import UserIcon
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length
from schemas.user_icon_schema import user_icon_schema, user_icons_schema

# Default route for all user icon requests
user_icon = Blueprint('user_icon', __name__, url_prefix='/usericon')

# Get request for all user icons
@user_icon.route('/', methods=['GET'])
def get_user_icons():
    user_icons = UserIcon.query.all()
    result = user_icons_schema.dump(user_icons)
    return jsonify(result)

# Get request for single user icon
@user_icon.route('/<int:user_icon_id>', methods=['GET'])
def get_user_icon(user_icon_id):
    user_icon = UserIcon.query.get(user_icon_id)
    result = user_icon_schema.dump(user_icon)
    return jsonify(result)

# # Get request for user icons of a specific user
# @user_icon.route('/user/<int:user_id><int:user_icon_id>', methods=['GET'])
# def get_user_icons_by_id(user_id,user_icon_id):
#     user_icons = UserIcon.filter_by(user_id).get(user_icon_id)
#     result = user_icons_schema.dump(user_icons)
#     return jsonify(result)






@user_icon.route('/create', methods=['POST'])
def new_icon():
    icon_fields = user_icon_schema.load(request.json)
    icon = UserIcon(
        user_icon_url = icon_fields ['user_icon_url'],
    )

    db.session.add(icon)
    db.session.commit()
    return jsonify((user_icon_schema).dump(icon))