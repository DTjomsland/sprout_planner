from main import db
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship


class Users(db.Model):
    __tablename__="users"
    
    # User columns
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, unique=True)
    user_password = db.Column(db.String(60))
    admin = db.Column(db.Boolean, default=False)
    activities = db.relationship("UserActivity", backref ='user')