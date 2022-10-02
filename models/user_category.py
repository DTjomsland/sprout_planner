from main import db

class UserCategory(db.Model):
    __tablename__="user_category"
    
    # User category columns
    user_category_id = db.Column(db.Integer, primary_key=True)
    user_category_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    activities = db.relationship(
        "UserActivity",
        backref = "category",
        # Ensure the children of the category are deleted when the category is
        cascade="all, delete-orphan"
    )