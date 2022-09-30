from main import db

class UserActivity(db.Model):
    __tablename__="user_activity"
    
    # User activity columns
    user_activity_id = db.Column(db.Integer, primary_key=True)
    user_activity_name = db.Column(db.String)
    user_category_id = db.Column(db.Integer,  db.ForeignKey('user_category.user_category_id'), nullable=False)
    icons = db.relationship(
        "UserIcon",
        backref = "activity"
    )
