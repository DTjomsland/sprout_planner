from main import db

class Icon(db.Model):
    __tablename__="icon"
    
    # Icon columns
    icon_id = db.Column(db.Integer, primary_key=True)
    icon_url = db.Column(db.String, nullable=False)
   