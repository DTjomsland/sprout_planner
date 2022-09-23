from main import db

class Activity(db.Model):
    __tablename__="activity"
    
    # Activity columns
    activity_id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String)
    icon_id = db.Column(db.Integer, db.ForeignKey('icon.icon_id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'),nullable=False)
    