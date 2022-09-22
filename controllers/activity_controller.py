from flask import Blueprint, jsonify, request, abort
from main import db
from models.activity import Activity
from schemas.activity_schema import activity_schema, activities_schema

# Default route for all activity requests
activity = Blueprint('activity', __name__, url_prefix='/activity')

# Get request for all pre-designed activities
@activity.route('/default', methods=['GET'])
def get_activities():
    activities = Activity.query.all()
    result = activities_schema.dump(activities)
    return jsonify(result.data)

