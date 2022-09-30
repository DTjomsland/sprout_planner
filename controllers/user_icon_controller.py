import os
from flask import Blueprint, jsonify, request, Flask, render_template
from main import db, create_app
from models.user_icon import UserIcon
from schemas.user_icon_schema import user_icon_schema, user_icons_schema

# Default route for all user icon requests
user_icon = Blueprint('user_icon', __name__, url_prefix='/usericon')

# Get request for all user icons
# Get request for all user activities
@user_icon.route('/<int:user_activity_id>', methods=['GET'])
def get_user_icons(user_activity_id):
    user_icons = db.session.query(UserIcon).with_entities(UserIcon.user_icon_url).filter(UserIcon.user_activity_id == user_activity_id)
    result = user_icons_schema.dump(user_icons)
    return jsonify(result)
