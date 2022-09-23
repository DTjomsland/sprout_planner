from main import ma
from marshmallow.validate import Length
from marshmallow import fields
from schemas.user_activity_schema import UserActivitySchema

#Schema for user table
class UserSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'user_email', 'user_password', 'admin', 'activities']
    password = ma.String(validate=Length(min=8))
    activity = fields.Nested(UserActivitySchema)
# Single user icon schema
user_schema = UserSchema()
# Multiple user icon schema
users_schema = UserSchema(many=True)
