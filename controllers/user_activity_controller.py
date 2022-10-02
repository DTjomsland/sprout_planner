from main import db
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError
from models.user_activity import UserActivity
from schemas.user_activity_schema import user_activity_schema, user_activities_schema

# Default route for all user activity requests
user_activity = Blueprint('user_activity', __name__, url_prefix='/useractivity')


# Get request for user activities based on category (Cateogires are attached to users)
@user_activity.route('/<int:user_category_id>', methods=['GET'])
def get_user_activities(user_category_id):
    # Search for all instances in the activity table where a row contains the category_id
    # Filter results so only ids/activity names are returned
    user_activities = db.session.query(UserActivity).with_entities(UserActivity.user_activity_id, UserActivity.user_activity_name).filter(UserActivity.user_category_id == user_category_id)
    # Returns jsonified activities for the specific category
    result = user_activities_schema.dump(user_activities)
    return jsonify(result)


# Post a new activity into the user activity table using associated category 
@user_activity.route('/<int:user_category_id>/create', methods=['POST'])
@jwt_required()
def new_activity(user_category_id):
    # Rename category ID from route
    category = user_category_id
    # Takes in data from the POST
    activity_fields = user_activity_schema.load(request.json)
    # Check to see if the activity exists for user/return error if it does 
    activity_check = UserActivity.query.filter_by(user_category_id = category, user_activity_name = activity_fields["user_activity_name"]).first()
    if activity_check:
        return {"error": "An activity with that name already exists."}
    # Creates a new activity object from entered information.
    activity = UserActivity(
        user_activity_name = activity_fields ['user_activity_name'],
        user_category_id = category
    )
    # Stage changes to the database
    db.session.add(activity)
    # Save the changes in the database
    db.session.commit()
    return jsonify((user_activity_schema).dump(activity))

# Update a specific user activity name
@user_activity.route("/<int:user_category_id>/<int:activity_id>", methods=["PUT"])
@jwt_required()
def update_activity(user_category_id, activity_id):
    # Rename category ID from route
    category = user_category_id
    # Find the activity in the database. Return error if it doesn't exist
    activity = UserActivity.query.get(activity_id)
    if not activity:
        return {"error": "Activity does no exist."}, 404
    # Retrieve the activity details 
    activity_fields = user_activity_schema.load(request.json)
    # Check to see if the activity exists for user/return error if it does 
    activity_check = UserActivity.query.filter_by(user_category_id = category, user_activity_name = activity_fields["user_activity_name"]).first()
    if activity_check:
        return {"error": "An activity with that name already exists."}
    # Update the activity name
    activity.user_activity_name = activity_fields["user_activity_name"]
    # Commit the changes to the database
    db.session.commit() 
    return jsonify(user_activity_schema.dump(activity)), 201  

# Delete user activity
@user_activity.route("/<int:activity_id>", methods=["DELETE"])
@jwt_required()
def delete_activity(activity_id):
    # Find the activity by id
    # Display error if activity is not found
    activity = UserActivity.query.get(activity_id)
    if not activity:
        return {"error": "Activity does not exist"}
    # Delete the activity from the database (Deletes all associated icons - cascade="all, delete-orphan)
    db.session.delete(activity)
    # Save the changes in the database
    db.session.commit()
    # Return message if deleted successfully
    return {"message": "Activity deleted successfully."}

# Validation error messages
@user_activity.errorhandler(ValidationError)
def register_validation_error(error):
    return error.messages, 400