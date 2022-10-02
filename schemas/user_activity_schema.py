from main import ma
from marshmallow import fields
from marshmallow.validate import Length
from schemas.user_icon_schema import UserIconSchema


# Schema for user activity table
class UserActivitySchema(ma.Schema):
    class Meta:
        fields = ['user_activity_id', 'user_activity_name', 'user_category_id', 'icons']
        load_only = ['icons']
    icons = fields.List(fields.Nested(UserIconSchema))

    # Validations
    user_activity_name = ma.String(required=True, validate=Length(min=1))

# single user activity schema
user_activity_schema = UserActivitySchema()

# Multiple user activity  schema
user_activities_schema = UserActivitySchema(many=True)