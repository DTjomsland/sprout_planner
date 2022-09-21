from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.icon import Icon
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length

icon = Blueprint('icon', __name__, url_prefix='/icon')

class IconSchema(ma.Schema):
    class Meta:
        fields = ('user_icon_id', 'icon_url')