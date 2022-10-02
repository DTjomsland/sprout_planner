from main import db
from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import get_jwt_identity, jwt_required
from models.user_feeling import UserFeeling
from schemas.user_feeling_schema import user_feeling_schema, user_feelings_schema

# Default route for all user feeling requests
user_feeling = Blueprint('user_feeling', __name__, url_prefix='/userfeeling')

# Get request for all user feelings for logged in user
@user_feeling.route('/', methods=['GET'])
# Requires token
@jwt_required()
def get_user_feelings():
    # Retrieve user information from jwt token
    user = get_jwt_identity()
    # Search for all instances in the feeling table where a row contains the user_id
    # Filter results so only ids/feeling names are returned
    feelings = db.session.query(UserFeeling).with_entities(UserFeeling.user_feeling_id, UserFeeling.user_feeling_name).filter(UserFeeling.user_id == user)
    # Returns jsonified feelings for the specific user
    result = user_feelings_schema.dump(feelings)
    return jsonify(result)


# Create user feeling
@user_feeling.route('/create', methods=['POST'])
# Requires token
@jwt_required()
def new_feeling():
    # Retrieve user information from jwt token
    user = get_jwt_identity()
    # Takes in data from the POST
    feeling_fields = user_feeling_schema.load(request.json)
    # Check to see if the feeling exists for user/return error if it does 
    feeling_check = UserFeeling.query.filter_by(user_id = user, user_feeling_name = feeling_fields["user_feeling_name"]).first()
    if feeling_check:
        return {"error": "A feeling with that name already exists."}
    # Creates a new user object from entered information.
    feeling = UserFeeling(
        user_feeling_name = feeling_fields ['user_feeling_name'],
        user_id = user
    )
    # Stage changes to the database
    db.session.add(feeling)
     # Save the changes in the database
    db.session.commit()
    return jsonify((user_feeling_schema).dump(feeling))

# Update a user feeling
@user_feeling.route("/<int:user_feeling_id>", methods=["PUT"])
@jwt_required()
def update_feeling(user_feeling_id):
    # Retrieve user information from jwt token
    user = get_jwt_identity()
    # Find the feeling in the database
    # Check to see if the feeling exists/return error if it does not
    feeling = UserFeeling.query.get(user_feeling_id)
    if not feeling:
        return {"error": "Feeling does not exist."}, 404
    # Retrieve the feeling details
    feeling_fields = user_feeling_schema.load(request.json)
    # Checks to see if the feeling already exists for specific user. Error if exists.
    feeling_check = UserFeeling.query.filter_by(user_id = user, user_feeling_name = feeling_fields["user_feeling_name"]).first()
    if feeling_check:
        return {"error": "A feeling with that name already exists."}
    # Update the feeling name
    feeling.user_feeling_name = feeling_fields["user_feeling_name"]
    # Commit the changes to the database
    db.session.commit() 
    return jsonify(user_feeling_schema.dump(feeling)), 201  

# Delete user feeling
@user_feeling.route("/<int:user_feeling_id>", methods=["DELETE"])
@jwt_required()
def delete_feeling(user_feeling_id):
    # Find the feeling in the database
    # Check to see if the feeling exists/return error if it does not
    feeling = UserFeeling.query.get(user_feeling_id)
    if not feeling:
        return {"error": "Feeling does not exist."}
    # Delete the feeling from the database (Deletes all associated feelings/icons - cascade="all, delete-orphan)
    db.session.delete(feeling)
    # Save the changes in the database
    db.session.commit()
    # Return message if deleted successfully
    return {"message": "Feeling deleted successfully."}

# Validation error messages
@user_feeling.errorhandler(ValidationError)
def register_validation_error(error):
    return error.messages, 400