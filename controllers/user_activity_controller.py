from flask import Blueprint, jsonify, request, abort
from main import db
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user_activity import UserActivity
from schemas.user_activity_schema import user_activity_schema, user_activities_schema

# Default route for all user activity requests
user_activity = Blueprint('user_activity', __name__, url_prefix='/useractivity')

# Get request for all user activities
@user_activity.route('/<int:user_category_id>', methods=['GET'])
def get_user_activities(user_category_id):
    user_activities = db.session.query(UserActivity).with_entities(UserActivity.user_activity_id, UserActivity.user_activity_name).filter(UserActivity.user_category_id == user_category_id)
    result = user_activities_schema.dump(user_activities)
    return jsonify(result)

# Post a new activity into the user activity table
@user_activity.route('/<int:user_category_id>/create', methods=['POST'])
@jwt_required()
def new_activity(user_category_id):
    category = user_category_id
    
    activity_fields = user_activity_schema.load(request.json)

    activity = UserActivity(
        user_activity_name = activity_fields ['user_activity_name'],
        user_category_id = category
    )

    db.session.add(activity)
    db.session.commit()
    return jsonify((user_activity_schema).dump(activity))

@user_activity.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_book(id):
    # Find the category in the database
    activity = UserActivity.query.get(id)
    # Check to see if the category exists
    if not activity:
        return {"error": "Activity does no exist."}, 404
    # Retrieve the category details from teh earlier request
    activity_fields = user_activity_schema.load(request.json)
    # Update the category name
    activity.user_activity_name = activity_fields["user_activity_name"]
    # Commit the changes to the database
    db.session.commit() 
    return jsonify(user_activity_schema.dump(activity)), 201  

# Delete user category
@user_activity.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_category(id):
    # Find the category by id
    activity = UserActivity.query.get(id)
    # Display error if category is not found
    if not activity:
        return {"error": "Activity not found"}
    # Delete the category from the database (Deletes all associated activities)
    db.session.delete(activity)
    # Save the changes in the database
    db.session.commit()
    # Return message if deleted successfully
    return {"message": "Activity deleted successfully"}
