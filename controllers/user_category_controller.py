from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.user_category import UserCategory
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length
from schemas.user_category_schema import user_category_schema, user_categories_schema

# Default route for all user category requests
user_category = Blueprint('user_category', __name__, url_prefix='/usercategory')

