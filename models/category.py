from main import db


class Category(db.Model):
    __tablename__="category"
    
    # Category columns
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String)
   
