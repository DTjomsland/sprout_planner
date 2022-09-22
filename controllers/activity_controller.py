from flask import Blueprint, jsonify, request, abort
from main import db, ma
from models.activity import Activity
from schemas.activity_schema import activity_schema, activities_schema


# Default route for all activity requests
activity = Blueprint('activity', __name__, url_prefix='/activity')

# Get request for all pre-designed activities
@activity.route('/', methods=['GET'])
def get_activities():
    activities = Activity.query.all()
    result = activities_schema.dump(activities)
    return jsonify(result)

# Get request for a single pre-designed activity
@activity.route('/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    activity = Activity.query.get(activity_id)
    result = activity_schema.dump(activity)
    return jsonify(result)