from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow.validate import Length
import psycopg2

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://david:Cygyxy64rtfg@localhost:5432/sprout_planner"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma = Marshmallow(app)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'user_email', 'user_password', 'admin')
    password = ma.String(validate=Length(min=8))

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# User table creation
class Users(db.Model):
    __tablename__="users"
    
    # User columns
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, unique=True, nullable=False)
    user_password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, default=False)

#Create the database tables
@app.cli.command('create')
def create_db():
    db.create_all()
    print("Creating tables...")

@app.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Dropped tables...")

# Seeding the database
@app.cli.command('seed')
def seed_db():
    users = Users(
        user_email="user@gmail.com",
        user_password="password"
    )

    db.session.add(users)

    admin = Users(
        user_email = "admin@gmail.com",
        user_password = "admin",
        admin = True
    )

    db.session.add(admin)

    db.session.commit()
    print("Seeding tables...")

@app.route('/')
def welcome():
    return "Sprout Planner under construction"

@app.route('/users')
def users():
    users_list = Users.query.all()
    result = users_schema.dump(users_list)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)