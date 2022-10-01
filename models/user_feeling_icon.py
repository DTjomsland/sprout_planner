from main import db

class UserFeelingIcon(db.Model):
    __tablename__="user_feeling_icon"
    
    # User feeling_icon columns
    user_feeling_icon_id = db.Column(db.Integer, primary_key=True)
    user_feeling_icon_url = db.Column(db.String)
    user_feeling_id = db.Column(db.Integer, db.ForeignKey("user_feeling.user_feeling_id"))