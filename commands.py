from flask import Blueprint
from main import db
from models.users import Users
from models.user_activity import UserActivity
from models.user_icon import UserIcon
from models.user_category import UserCategory
from models.user_feeling import UserFeeling
from models.user_feeling_icon import UserFeelingIcon
from main import bcrypt




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

    # Seeding first two users
    user1 = Users(
        user_email = "user@gmail.com",
        user_name = 'Scotty',
        user_password = bcrypt.generate_password_hash("password").decode("utf-8"),
    )

    db.session.add(user1)
    db.session.commit()

    user2 = Users(
        user_email = "user2@gmail.com",
        user_name = 'David',
        user_password = bcrypt.generate_password_hash("password").decode("utf-8"),
    )
    db.session.add(user2)
    db.session.commit()


    # Seeding categories
    category1 = UserCategory(
        user_category_name = "Activity",
        user_id = 1,
    )

    category2 = UserCategory(
        user_category_name = "Exercise",
        user_id = 1,
    )

    category3 = UserCategory(
        user_category_name = "Meal",
        user_id = 1,
    )

    category4 = UserCategory(
        user_category_name = "Activity",
        user_id = 2,
    )

    category5 = UserCategory(
        user_category_name = "Exercise",
        user_id = 2,
    )

    category6 = UserCategory(
        user_category_name = "Meal",
        user_id = 2,
    )

    db.session.add(category1)
    db.session.add(category2)
    db.session.add(category3)
    db.session.add(category4)
    db.session.add(category5)
    db.session.add(category6)
    db.session.commit()


# Seeding feelings
    feeling1 = UserFeeling(
        user_feeling_name = "Sad",
        user_id = 1,
    )

    feeling2 = UserFeeling(
        user_feeling_name = 'Happy',
        user_id = 1,
    )


    feeling3 = UserFeeling(
        user_feeling_name = 'Angry',
        user_id = 1,
    )

    feeling4 = UserFeeling(
        user_feeling_name = "Tired",
        user_id = 1,
    )

    feeling5 = UserFeeling(
        user_feeling_name = "Hungry",
        user_id = 2,
    )

    feeling6 = UserFeeling(
        user_feeling_name = "Mad",
        user_id = 2,
    )

    feeling7 = UserFeeling(
        user_feeling_name = "Sleepy",
        user_id = 2,
    )

    db.session.add(feeling1)
    db.session.add(feeling2)
    db.session.add(feeling3)
    db.session.add(feeling4)
    db.session.add(feeling5)
    db.session.add(feeling6)
    db.session.add(feeling7)
    

    # Seeding activities
    activity1 = UserActivity(
        user_activity_name = "Jogging",
        user_category_id = 2,
    )

    activity2 = UserActivity(
        user_activity_name = 'Swimming',
        user_category_id = 2,
    )


    activity3 = UserActivity(
        user_activity_name = 'Lasagna',
        user_category_id = 3,
    )

    activity4 = UserActivity(
        user_activity_name = "Reading",
        user_category_id = 4,
    )

    activity5 = UserActivity(
        user_activity_name = "Soccer",
        user_category_id = 5,
    )

    activity6 = UserActivity(
        user_activity_name = "Video Games",
        user_category_id = 4,
    )

    activity7 = UserActivity(
        user_activity_name = "Eggs",
        user_category_id = 6,
    )

    db.session.add(activity1)
    db.session.add(activity2)
    db.session.add(activity3)
    db.session.add(activity4)
    db.session.add(activity5)
    db.session.add(activity6)
    db.session.add(activity7)
    db.session.commit()


    # Seeding User Icon
    feelingicon1 =  UserFeelingIcon(
        user_feeling_icon_url = 'randomurl1',
        user_feeling_id = 1,
    )

    feelingicon2 =  UserFeelingIcon(
        user_feeling_icon_url = 'randomurl2',
        user_feeling_id = 2,
    )

    feelingicon3 =  UserFeelingIcon(
        user_feeling_icon_url = 'randomurl3',
        user_feeling_id = 3,
    )

    feelingicon4 =  UserFeelingIcon(
        user_feeling_icon_url = 'randomurl4',
        user_feeling_id = 4,
    )

    feelingicon5 =  UserFeelingIcon(
        user_feeling_icon_url = 'randomurl5',
        user_feeling_id = 5,
    )

    feelingicon5 =  UserFeelingIcon(
        user_feeling_icon_url = 'randomurl5',
        user_feeling_id = 6,
    )

    feelingicon5 =  UserFeelingIcon(
        user_feeling_icon_url = 'randomurl5',
        user_feeling_id = 7,
    )

    db.session.add(feelingicon1)
    db.session.add(feelingicon2)
    db.session.add(feelingicon3)
    db.session.add(feelingicon4)
    db.session.add(feelingicon5)
    

    # Seeding User Icon
    icon1 =  UserIcon(
        user_icon_url = 'randomurl1',
        user_activity_id = 1,
    )

    icon2 =  UserIcon(
        user_icon_url = 'randomurl2',
        user_activity_id = 2,
    )

    icon3 =  UserIcon(
        user_icon_url = 'randomurl3',
        user_activity_id = 3,
    )

    icon4 =  UserIcon(
        user_icon_url = 'randomurl4',
        user_activity_id = 4,
    )

    icon5 =  UserIcon(
        user_icon_url = 'randomurl5',
        user_activity_id = 5,
    )

    icon5 =  UserIcon(
        user_icon_url = 'randomurl5',
        user_activity_id = 6,
    )
    
    icon5 =  UserIcon(
        user_icon_url = 'randomurl6',
        user_activity_id = 7,
    )

    db.session.add(icon1)
    db.session.add(icon2)
    db.session.add(icon3)
    db.session.add(icon4)
    db.session.add(icon5)
    db.session.commit()

    print("Seeding tables...")