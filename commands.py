from flask import Blueprint
from main import db
from models.users import Users
from main import bcrypt
# from models.activity import Activity
# from models.user_activity import UserActivity
# from models.category import Category
# from models.user_category import UserCategory
# from models.icon import Icon
# from models.user_icon import UserIcon


db_commands = Blueprint("db", __name__)

@db_commands.cli.command('create')
def create_db():
    db.create_all()
    print("Creating tables...")

@db_commands.cli.command('drop')
def drop_db():
    db.drop_all()
    print("Dropping tables...")

@db_commands.cli.command('seed')
def seed_db():
    users = Users(
        user_email = "user@gmail.com",
        user_password = bcrypt.generate_password_hash("password").decode("utf-8"),
    )

    db.session.add(users)

    admin = Users(
        user_email = "admin@gmail.com",
        user_password = bcrypt.generate_password_hash("password").decode("utf-8"),
        admin = True
    )

    db.session.add(admin)

    db.session.commit()
    print("Seeding tables...")