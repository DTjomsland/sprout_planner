from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.user_category import UserCategory
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length

user_category = Blueprint('user_category', __name__, url_prefix='/usercategory')

class UserCategorySchema(ma.Schema):
    class Meta:
        fields = ('user_category_id', 'user_category_name'),