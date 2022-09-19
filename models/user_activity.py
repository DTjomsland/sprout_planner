from main import db

class UserActivity(db.Model):
    __tablename__="user_activity"
    
    # User columns
    user_activity_id = db.Column(db.Integer, primary_key=True)
    user_activity_name = db.Column(db.String, nullable=False)
    user_icon_id = db.Column(db.Integer, nullable=False)
    icon_id = db.Column(db.Integer, nullable=False)
    user_category_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    