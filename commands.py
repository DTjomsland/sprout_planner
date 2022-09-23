from random import seed
from flask import Blueprint
from main import db
from models.users import Users
from main import bcrypt
from models.activity import Activity
from models.user_activity import UserActivity
from models.category import Category
from models.user_category import UserCategory
from models.icon import Icon
from models.user_icon import UserIcon


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
    # Seeding first user
    user1 = Users(
        user_email = "user@gmail.com",
        user_password = bcrypt.generate_password_hash("password").decode("utf-8"),
    )

    db.session.add(user1)
    db.session.commit()
    
    #Seeding first admin
    admin = Users(
        user_email = "admin@gmail.com",
        user_password = bcrypt.generate_password_hash("password").decode("utf-8"),
        admin = True
    )
    db.session.add(admin)
    db.session.commit()


    # Seeding Icons (Function repeats seed process for each url)
    def seed_icon():
        icons = (
        'custom',
        'https://res.cloudinary.com/dydrnv83j/image/upload/v1663745223/Sprout%20Icons/pngaaa.com-628479_wtnlk4.png', 
        'https://res.cloudinary.com/dydrnv83j/image/upload/v1663745220/Sprout%20Icons/clipart1515874_kqhliw.png', 
        'https://res.cloudinary.com/dydrnv83j/image/upload/v1663745216/Sprout%20Icons/clipart13444_tmhvfr.png', 
        'https://res.cloudinary.com/dydrnv83j/image/upload/v1663745215/Sprout%20Icons/clipart16521_zt8qrg.png', 
        'https://res.cloudinary.com/dydrnv83j/image/upload/v1663745215/Sprout%20Icons/pngaaa.com-716354_vacdsl.png', 
        'https://res.cloudinary.com/dydrnv83j/image/upload/v1663745215/Sprout%20Icons/clipart129344_f2so1h.png',
        'https://res.cloudinary.com/dydrnv83j/image/upload/v1663745215/Sprout%20Icons/NicePng_basketball-clip-art-png_2919530_nppqyg.png',
        'https://res.cloudinary.com/dydrnv83j/image/upload/v1663745215/Sprout%20Icons/clipart27326_bosnvu.png'
        )

        for i in icons:
            icon = Icon(
                icon_url = i, 
            )
            db.session.add(icon)
    db.session.commit()
    seed_icon()

    # Seeding Category (Function repeats seed process for each category)
    def seed_category():
        categories = ('custom','activity', 'exercise', 'breakfast', 'lunch', 'dinner')
        for i in categories:
            category = Category(
                category_name = i, 
            )
            db.session.add(category)
    seed_category()
    db.session.commit()

    # Seeding Activities
    custom = Activity(
        activity_name = 'custom',
        icon_id = 1,
        category_id = 1,
    )

    videogames = Activity(
        activity_name = 'Play Video Games',
        icon_id = 6,
        category_id = 2, 
    )

    car = Activity(
        activity_name = "Car Ride",
        icon_id = 3,
        category_id = 2,
    )

    soccer = Activity(
        activity_name = "Play Golf",
        icon_id = 8,
        category_id = 3,
    )

    walk = Activity(
        activity_name = "Go for a Walk",
        icon_id = 4,
        category_id = 3,
    )

    db.session.add(custom)
    db.session.add(videogames)
    db.session.add(car)
    db.session.add(soccer)
    db.session.add(walk)
    db.session.commit()

    # Seeding User Icon
    def seed_user_icon():
        user_icons = ('default','randomurl', 'randomurl2', 'randomurl3')
        for i in user_icons:
            user_icon = UserIcon(
                user_icon_url = i, 
            )
            db.session.add(user_icon)
    seed_user_icon()
    db.session.commit()

    #Seeding User Category
    def seed_user_category():
        user_categories = ('default','randomcat', 'randomcat', 'randomcat')
        for i in user_categories:
            user_category = UserCategory(
                user_category_name = i, 
            )
            db.session.add(user_category)
    seed_user_category()
    db.session.commit()
    
    # Seeding User Activity
    
    default = UserActivity(
        user_activity_name = 'default',
        user_icon_id = 1,
        icon_id = 2,
        user_category_id = 1,
        category_id = 2,
        user = admin,
    )
    db.session.add(default)

    jog = UserActivity(
        user_activity_name = 'Jog',
        user_icon_id = 2,
        icon_id = 1,
        user_category_id = 2,
        category_id = 1,
        user = user1,
    )
    db.session.add(jog)
    db.session.commit()
    print("Seeding tables...")