from main import db

class Users(db.Model):
    __tablename__="users"
    
    # User columns
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, unique=True, nullable=False)
    user_password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False)