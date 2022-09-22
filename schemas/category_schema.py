from main import ma

# Category table Schema
class CategorySchema(ma.Schema):
    class Meta:
        fields = ('category_id', 'category_name'),

# single category schema
category_schema = CategorySchema()
# multiple category schema
categories_schema = CategorySchema(many=True)