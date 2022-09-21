from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.activity import Activity

activity = Blueprint('activity', __name__, url_prefix='/activity')

class ActivitySchema(ma.Schema):
    class Meta:
        fields = ('activity_id', 'activity_name', ' icon_id', 'icon_id', 'category_id'),