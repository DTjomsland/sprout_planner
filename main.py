from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://david:Cygyxy64rtfg@localhost:5432/sprout_planner"

class Users(db.Model):
        __tablename__="users"

        id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def welcome():
    return "Sprout Planner under construction"