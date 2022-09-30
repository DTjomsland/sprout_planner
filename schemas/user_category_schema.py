from main import ma
from marshmallow import fields
from marshmallow.validate import Length
from schemas.user_activity_schema import UserActivitySchema
# Schema for user category table
class UserCategorySchema(ma.Schema):
    class Meta:
        fields = ['user_category_id', 'user_category_name', 'user_id', 'activities']
    activities = fields.List(fields.Nested(UserActivitySchema,  only = ["user_activity_name", "icons"]))
# single user category schema
user_category_schema = UserCategorySchema()

# Multiple user category schema
user_categories_schema = UserCategorySchema(many=True)