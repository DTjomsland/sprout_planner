from main import db

class UserIcon(db.Model):
    __tablename__="user_icon"
    
    # User icon columns
    user_icon_id = db.Column(db.Integer, primary_key=True)
    user_icon_url = db.Column(db.String)
    user_activity_id = db.Column(db.Integer, db.ForeignKey("user_activity.user_activity_id"), nullable=False, unique=True)