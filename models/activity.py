from main import db

class Activity(db.Model):
    __tablename__="activity"
    
    # User columns
    activity_id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String, nullable=False)
    icon_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)