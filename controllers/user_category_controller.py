from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.user_category import UserCategory
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length
from schemas.user_category_schema import user_category_schema, user_categories_schema

# Default route for all user category requests
user_category = Blueprint('user_category', __name__, url_prefix='/usercategory')

# Get request for all user categories
@user_category.route('/', methods=['GET'])
def get_user_categories():
    user_categories = UserCategory.query.all()
    result = user_categories_schema.dump(user_categories)
    return jsonify(result)

# Get request for single user category
@user_category.route('/<int:user_category_id>', methods=['GET'])
def get_user_category(user_category_id):
    user_category = UserCategory.query.get(user_category_id)
    result = user_category_schema.dump(user_category)
    return jsonify(result)

@user_category.route('/create', methods=['POST'])
def new_category():
    category_fields = user_category_schema.load(request.json)
    category = UserCategory(
        user_category_name = category_fields ['user_category_name'],
    )

    db.session.add(category)
    db.session.commit()
    return jsonify((user_category_schema).dump(category))