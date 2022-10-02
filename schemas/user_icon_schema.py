from main import ma

# Schema for user icons table
class UserIconSchema(ma.Schema):
    class Meta:
        fields = ['user_icon_id', 'user_icon_url', 'user_activity_id']
        load_only = ['user_activity_id']

# Single user icon schema
user_icon_schema = UserIconSchema()

# Multiple user icon schema
user_icons_schema = UserIconSchema(many=True)