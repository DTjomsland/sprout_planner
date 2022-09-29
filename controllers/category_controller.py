from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.category import Category
from marshmallow.validate import Length
from schemas.category_schema import category_schema, categories_schema

# Default route for all category requests
category = Blueprint('category', __name__, url_prefix='/category')

# Get request for all pre-designed categories
@category.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    result = categories_schema.dump(categories)
    return jsonify(result)

# Get request for a single pre-designed category
@category.route('/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = Category.query.get(category_id)
    result = category_schema.dump(category)
    return jsonify(result)