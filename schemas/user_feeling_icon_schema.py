from main import ma

# Schema for user icons table
class UserFeelingIconSchema(ma.Schema):
    class Meta:
        fields = ['user_feeling_icon_id', 'user_feeling_icon_url', 'user_feeling_id']
        load_only = ['user_feeling_id']
        
# single user icon schema
user_feeling_icon_schema = UserFeelingIconSchema()

# Multiple user icon schema
user_feeling_icons_schema = UserFeelingIconSchema(many=True)