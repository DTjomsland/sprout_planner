from main import ma

#Schema for Icons table
class IconSchema(ma.Schema):
    class Meta:
        fields = ('user_icon_id', 'icon_url')

# single category schema
icon_schema = IconSchema()

# Multiple category schema
icons_schema = IconSchema(many=True)