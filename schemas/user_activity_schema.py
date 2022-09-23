from main import ma
from marshmallow import fields


# Schema for user activity table
class UserActivitySchema(ma.Schema):
    class Meta:
        fields = ['user_activity_id', 'user_activity_name', 'user_icon_id', 'icon_id', 'user_category_id', 'category_id', 'user_id']


# single user activity schema
user_activity_schema = UserActivitySchema()

# Multiple user activity  schema
user_activities_schema = UserActivitySchema(many=True)