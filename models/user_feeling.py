from main import db

class UserFeeling(db.Model):
    __tablename__="user_feeling"
    
    # User feeling columns
    user_feeling_id = db.Column(db.Integer, primary_key=True)
    user_feeling_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    feeling_icon = db.relationship(
        "UserFeelingIcon",
        backref = "feeling",
        # Ensure the children of the feeling are deleted when the feeling is
        cascade="all, delete-orphan"
    )