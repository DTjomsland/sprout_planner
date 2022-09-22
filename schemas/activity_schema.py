from main import ma

class ActivitySchema(ma.Schema):
    class Meta:
        fields = ('activity_id', 'activity_name', ' icon_id', 'icon_id', 'category_id'),


# single activity schema
activity_schema = ActivitySchema()

# multiple activity schema
activities_schema = ActivitySchema(many=True)