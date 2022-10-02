from main import ma
from marshmallow.validate import Length, Email, ContainsOnly
from marshmallow import fields
from schemas.user_category_schema import UserCategorySchema
from schemas.user_feeling_schema import UserFeelingSchema

#Schema for user table
class UserSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'user_name', 'user_email', 'user_password', 'categories', 'user_feelings']
        load_only = ['user_id', 'user_email', 'user_password', 'admin']
    password = ma.String(validate=Length(min=8))
    categories = fields.List(fields.Nested(UserCategorySchema,  only = ["user_category_name", "activities"]))
    user_feelings = fields.List(fields.Nested(UserFeelingSchema))

    # Validations
    user_name = ma.String(required=True, validate=Length(min=1))
    user_email = ma.Email(required=True)
    user_password = ma.String(required=True,  validate=Length(min=8))
    
# Single user icon schema
user_schema = UserSchema()
# Multiple user icon schema
users_schema = UserSchema(many=True)

