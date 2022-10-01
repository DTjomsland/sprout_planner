from main import ma, db
from marshmallow.validate import Length
from marshmallow import fields
from schemas.user_category_schema import UserCategorySchema
from schemas.user_feeling_schema import UserFeelingSchema

#Schema for user table
class UserSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'user_name', 'user_email', 'user_password', 'admin', 'categories', 'user_feelings']
        load_only = ['user_id', 'user_email', 'user_password', 'admin']
    password = ma.String(validate=Length(min=8))
    categories = fields.List(fields.Nested(UserCategorySchema,  only = ["user_category_name", "activities"]))
    user_feelings = fields.List(fields.Nested(UserFeelingSchema))
# Single user icon schema
user_schema = UserSchema()
# Multiple user icon schema
users_schema = UserSchema(many=True)
