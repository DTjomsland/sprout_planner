from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.user_activity import UserActivity
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length
from schemas.user_activity_schema import user_activity_schema, user_activities_schema

# Default route for all user activity requests
user_activity = Blueprint('user_activity', __name__, url_prefix='/useractivity')

# Get request for all user activities
@user_activity.route('/', methods=['GET'])
def get_user_activities():
    user_activities = UserActivity.query.all()
    result = user_activities_schema.dump(user_activities)
    return jsonify(result)

# Get request for single user activity
@user_activity.route('/<int:user_activity_id>', methods=['GET'])
def get_user_activity(user_activity_id):
    user_activity = UserActivity.query.get(user_activity_id)
    result = user_activity_schema.dump(user_activity)
    return jsonify(result)



# Post a new activity into the user activity table
@user_activity.route('/create', methods=['POST'])
def new_activity():
    activity_fields = user_activity_schema.load(request.json)
    activity = UserActivity(
        user_activity_name = activity_fields["user_activity_name"],
        user_icon_id = activity_fields['user_icon_id'],
        icon_id = activity_fields['icon_id'],
        user_category_id = activity_fields['user_category_id'],
        category_id = activity_fields['category_id'],
        user_id = activity_fields['user_id']
    )

    db.session.add(activity)
    db.session.commit()
    return jsonify((user_activity_schema).dump(activity))