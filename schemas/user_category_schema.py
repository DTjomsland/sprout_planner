from main import ma

# Schema for user category table
class UserCategorySchema(ma.Schema):
    class Meta:
        fields = ('user_category_id', 'user_category_name')

# single user category schema
user_category_schema = UserCategorySchema()

# Multiple user category schema
user_categories_schema = UserCategorySchema(many=True)