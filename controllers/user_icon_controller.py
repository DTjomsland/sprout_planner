from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.user_icon import UserIcon
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length

user_icon = Blueprint('user_icon', __name__, url_prefix='/usericon')

class UserCategorySchema(ma.Schema):
    class Meta:
        fields = ('user_icon_id', 'user_icon_name'),