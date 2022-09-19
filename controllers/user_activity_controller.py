from flask import Blueprint, jsonify, request, abort
from main import db, bcrypt, ma
from models.user_activity import UserActivity
from flask_jwt_extended import  create_access_token
from marshmallow.validate import Length

user_activity = Blueprint('user_activity', __name__, url_prefix='/useractivity')

class UserActivitySchema(ma.Schema):
    class Meta:
        fields = ('user_activity_id', ' user_activity_name', 'user_icon_id', 'icon_id', 'user_category_id', 'category_id', 'user_id' )

# user_activity_schema = UserActivitySchema()
# user_activities_schema = UserActivitySchema(many=True)

# @user_activity.route('/create', methods=['GET'])
# def create_activity():
   
#     user_fields = user_activity_schema.load(request.json)
#     print(user_fields["user_email"])
#     print(user_fields["user_password"])

#     activity = UserActivity(
#         user_activity_name = user_fields["user_activity_name"],
#         user_icon_id = user_fields["user_icon_id"],
#         user_activity_name = user_fields["user_activity_name"],
#         user_icon_id = user_fields["user_icon_id"],
#         user_activity_name = user_fields["user_activity_name"],
#         user_icon_id = user_fields["user_icon_id"],
#         user_icon_id = user_fields["user_icon_id"]
#    )

#     db.session.add(activity)

#     db.session.commit()
#     return jsonify((user_activity_schema).dump(activity))