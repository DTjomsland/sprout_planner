from main import ma
from marshmallow.validate import Length

#Schema for user table
class UserSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'user_email', 'user_password', 'admin']
    password = ma.String(validate=Length(min=8))

# Single user icon schema
user_schema = UserSchema()
# Multiple user icon schema
users_schema = UserSchema(many=True)
