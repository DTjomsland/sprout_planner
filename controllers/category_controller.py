from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.category import Category
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length
from schemas.category_schema import category_schema, categories_schema

# Default route for all category requests
category = Blueprint('category', __name__, url_prefix='/category')