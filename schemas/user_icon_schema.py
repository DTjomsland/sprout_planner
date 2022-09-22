from main import ma

# Schema for user icons table
class UserIconSchema(ma.Schema):
    class Meta:
        fields = ['user_icon_id', 'user_icon_name']

# single user icon schema
user_icon_schema = UserIconSchema()

# Multiple user icon schema
user_icons_schema = UserIconSchema(many=True)