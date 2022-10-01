from main import ma
from marshmallow import fields
from marshmallow.validate import Length
from schemas.user_feeling_icon_schema import UserFeelingIconSchema
# Schema for user category table
class UserFeelingSchema(ma.Schema):
    class Meta:
        fields = ['user_feeling_id', 'user_feeling_name', 'user_id', 'feeling_icon']
    feeling_icon = fields.List(fields.Nested(UserFeelingIconSchema))

# single user category schema
user_feeling_schema = UserFeelingSchema()

# Multiple user category schema
user_feelings_schema = UserFeelingSchema(many=True)