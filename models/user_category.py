from main import db
from flask import jsonify, request
import jwt
from functools import wraps

class UserCategory(db.Model):
    __tablename__="user_category"
    
    # User category columns
    user_category_id = db.Column(db.Integer, primary_key=True)
    user_category_name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    activities = db.relationship(
        "UserActivity",
        backref = "category"
    )

def token_required(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token = None
            if 'x-access-tokens' in request.headers:
                token = request.headers['x-access-tokens']
 
            if not token:
                return jsonify({'message': 'a valid token is missing'})
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                current_user = Users.query.filter_by(public_id=data['public_id']).first()
            except:
                return jsonify({'message': 'token is invalid'})
 
            return f(current_user, *args, **kwargs)
        return decorator