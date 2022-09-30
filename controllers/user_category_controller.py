from flask import Blueprint, jsonify, request
from main import db
from models.user_category import UserCategory
from models.users import Users
from flask_jwt_extended import get_jwt_identity, jwt_required
from marshmallow.validate import Length
import jwt
from schemas.user_category_schema import user_category_schema, user_categories_schema

# Default route for all user category requests
user_category = Blueprint('user_category', __name__, url_prefix='/usercategory')

# Get request for all user categories
@user_category.route('/', methods=['GET'])
@jwt_required()
def get_user_categories():

    # Display all categories for the current user
    user = get_jwt_identity()
    # categories = UserCategory.query.filter(UserCategory.user_id == user)
    categories = db.session.query(UserCategory).with_entities(UserCategory.user_category_name).filter(UserCategory.user_id == user)
    result = user_categories_schema.dump(categories)
    return jsonify(result)

# Create user category
@user_category.route('/create', methods=['POST'])
def new_category():
    category_fields = user_category_schema.load(request.json)
    category = UserCategory(
        user_category_name = category_fields ['user_category_name'],
    )

    db.session.add(category)
    db.session.commit()
    return jsonify((user_category_schema).dump(category))