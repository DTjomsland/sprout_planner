from main import db

class UserIcon(db.Model):
    __tablename__="user_icon"
    
    # User icon columns
    user_icon_id = db.Column(db.Integer, primary_key=True)
    user_icon_url = db.Column(db.String)
   