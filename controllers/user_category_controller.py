from main import db
from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow.exceptions import ValidationError
from models.user_category import UserCategory
from schemas.user_category_schema import user_category_schema, user_categories_schema

# Default route for all user category requests
user_category = Blueprint('user_category', __name__, url_prefix='/usercategory')

# Get request for all user categories for logged in user
@user_category.route('/', methods=['GET'])
# Requires token
@jwt_required()
def get_user_categories():
    # Retrieve user information from jwt token
    user = get_jwt_identity()
    # Search for all instances in the category table where a row contains the user_id
    # Filter results so only ids/category names are returned
    categories = db.session.query(UserCategory).with_entities(UserCategory.user_category_id, UserCategory.user_category_name).filter(UserCategory.user_id == user)
    # Returns jsonified categories for the specific user
    result = user_categories_schema.dump(categories)
    return jsonify(result)

# Create user category
@user_category.route('/create', methods=['POST'])
# Requires token
@jwt_required()
def new_category():
    # Retrieve user information from jwt token
    user = get_jwt_identity()
    # Takes in data from the POST
    category_fields = user_category_schema.load(request.json)
    # Check to see if the category exists for user/return error if it does 
    category_check = UserCategory.query.filter_by(user_id = user, user_category_name = category_fields["user_category_name"]).first()
    if category_check:
        return {"error": "A category with that name already exists."}
    # Creates a new user object from entered information.
    category = UserCategory(
        user_category_name = category_fields ['user_category_name'],
        user_id = user
    )
    # Stage changes to the database
    db.session.add(category)
     # Save the changes in the database
    db.session.commit()
    return jsonify((user_category_schema).dump(category))

# Update a user category
@user_category.route("/<int:user_category_id>", methods=["PUT"])
@jwt_required()
def update_category(user_category_id):
    # Retrieve user information from jwt token
    user = get_jwt_identity()
    # Find the category in the database
    # Check to see if the category exists/return error if it does not
    category = UserCategory.query.get(user_category_id)
    if not category:
        return {"error": "Category does not exist."}, 404
    # Retrieve the category details
    category_fields = user_category_schema.load(request.json)
    # Checks to see if the category already exists for specific user. Error if exists.
    category_check = UserCategory.query.filter_by(user_id = user, user_category_name = category_fields["user_category_name"]).first()
    if category_check:
        return {"error": "A category with that name already exists."}
    # Update the category name
    category.user_category_name = category_fields["user_category_name"]
    # Commit the changes to the database
    db.session.commit() 
    return jsonify(user_category_schema.dump(category)), 201  

# Delete user category
@user_category.route("/<int:user_category_id>", methods=["DELETE"])
@jwt_required()
def delete_category(user_category_id):
    # Find the category in the database
    # Check to see if the category exists/return error if it does not
    category = UserCategory.query.get(user_category_id)
    if not category:
        return {"error": "Category does not exist."}
    # Delete the category from the database (Deletes all associated activities/icons - cascade="all, delete-orphan)
    db.session.delete(category)
    # Save the changes in the database
    db.session.commit()
    # Return message if deleted successfully
    return {"message": "Category deleted successfully."}

# Validation error messages
@user_category.errorhandler(ValidationError)
def register_validation_error(error):
    return error.messages, 400