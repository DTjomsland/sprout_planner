from main import db

class UserCategory(db.Model):
    __tablename__="user_category"
    
    # User category columns
    user_category_id = db.Column(db.Integer, primary_key=True)
    user_category_name = db.Column(db.String)
    user_id = db.Column(db.Integer)
    activities = db.relationship("UserActivity", backref ='category')