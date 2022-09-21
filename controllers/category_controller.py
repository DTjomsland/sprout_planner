from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.category import Category
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length

category = Blueprint('category', __name__, url_prefix='/category')

class UserCategorySchema(ma.Schema):
    class Meta:
        fields = ('category_id', 'category_name'),