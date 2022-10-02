from main import db


class Users(db.Model):
    __tablename__="users"
    
    # User columns
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255))
    user_email = db.Column(db.String, unique=True)
    user_password = db.Column(db.String(60))
    categories = db.relationship(
        "UserCategory",
        backref= "user",
        # Ensure the children of the feeling are deleted along with
        cascade="all, delete-orphan"
    )
    feelings = db.relationship(
        "UserFeeling",
        backref= "user",
        # Ensure the children of the feeling are deleted along with
        cascade="all, delete-orphan"
    )
    