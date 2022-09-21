from main import db

class UserActivity(db.Model):
    __tablename__="user_activity"
    
    # User activity columns
    user_activity_id = db.Column(db.Integer, primary_key=True)
    user_activity_name = db.Column(db.String, nullable=False)
    user_icon_id = db.Column(db.Integer, db.ForeignKey('user_icon.user_icon_id'), nullable=False)
    icon_id = db.Column(db.Integer, db.ForeignKey('icon.icon_id'), nullable=False)
    user_category_id = db.Column(db.Integer,  db.ForeignKey('user_category.user_category_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    