from main import ma
from marshmallow import fields
from marshmallow.validate import Length
from schemas.user_feeling_icon_schema import UserFeelingIconSchema


# Schema for user feeling table
class UserFeelingSchema(ma.Schema):
    class Meta:
        fields = ['user_feeling_id', 'user_feeling_name', 'user_id', 'feeling_icon']
        load_only = ['feeling_icon']
    feeling_icon = fields.List(fields.Nested(UserFeelingIconSchema))

    # Validations
    user_feeling_name = ma.String(required=True, validate=Length(min=1))

# Single user feeling schema
user_feeling_schema = UserFeelingSchema()

# Multiple user feeling schema
user_feelings_schema = UserFeelingSchema(many=True)