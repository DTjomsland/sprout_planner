# Api Webserver Project
## Overview
This API provides data for a simple daily planner that has an intended audience of those with special needs/disabilities.  The API allows the user to create accounts through an email sign-up process.  Once signed up, the user can create categories for the types of tasks/acitivites they like to do on a daily basis.  After a category is created, the user can add activities to the category.  For example: The user creates a category named "Exercise" and adds "Swimming", "Jogging", and "Soccer."  Upon creation of an activity, the user will have the option of uploading an image to use as a visual representation of the activity.  This information is intended to be displayed in a user friendly interface that allows for the user to plan their day and act as a means of communication. Along with the create, read, update and delete ability of the daily planner comes a feature that allows the user to create feelings and assign visual representations of them.  This is intended to be displayed in a similar way as the activities, acting as a way for the user to communicate how they are currently feeling.

<br>



### Intended Use of Account Creation Features:

![image](images/sproutimg.PNG)

<br>



### Intended Use of Category Creation and Editing Features:

![image](images/sproutimg3.PNG)

<br>



### Intended Use of Category Creation and Editing Features:

![image](images/sproutimg4.PNG)

<br>



### Intended Use of the Data Overall:

![image](images/sproutimg2.PNG)

<br>



## Identification of the Problem
The problem I am trying to solve with this application is the lack of a means for some with special needs/disabilities to communicate their feelings and how they want their day to be structured. During my time as a high school special needs teacher and  as a support worker, I've worked with countless individuals that are unable to communicate through speech, often needing visual help to communicate.  This application intends to provide a way for those who are unable to communicate verbally to gain autonomy by providing them a way to communicate their feelings, as well as the structure of their day.

<br>



## Why It Needs to be Solved

This problem needs to be solved because far too many individuals are unable to communicate their feelings and wants verbally. After my time in the disabilities sector, I've noticed many individuals with disabilities are often times coasting through their days, doing what others want them to do because they are unable to communicate what they want and feel. This often leads to frustration and a feeling of helplessness. Everyone deserves a voice, and this API intends on facilitating that.

<br>

## Chosen Database System

The database system used for this API is PostgreSQL.  PostgreSQL is an open source object-relational database system that utilizes the SQL language.  I chose PostgreSQL due to it's track record  of being scalable, secure, and ensuring data integrity. PostgreSQL is also beginner friendly. Since this is my first API, that played a large role in choosing it. 

Despite the benefits, their are some drawbacks to choosing PostgreSQL.  In regards to performance, PostgreSQL is slower than competitors such as MySQL. PostgreSQL places compatibility at the top of it's list, so changes for improvements in speed are more involved than its competitors. Overall, I found PostgreSQL easy to work with despite being rather green in the API world.

<br>

## Third Party Services:
### Cloudinary
This application utilizes Cloudinary for its image uploading and storage. In the routes `/usericon/\<int:user_activity_id>/upload` and `/userfeelingicon/\<int:user_feeling_id>/upload`, the Cloudinary Upload API is called which is configured with a full set of my user credentials which are stored safely in the .env file. The Cloudinary Upload API allows for the user to upload images to Cloudinary which returns information regarding the upload.  In this case, the URL is taken from the returned information and is used to create a new row in the UserIcon and UserFeelingIcon tables. 

### Flask Packages
- alembic==1.7.7
- bcrypt==4.0.0
- certifi==2022.9.24
- click==8.0.4
- cloudinary==1.30.0
- dataclasses==0.8
- Flask==2.0.3
- Flask-Bcrypt==1.0.1
- Flask-Cors==3.0.10
- Flask-JWT-Extended==4.4.2
- flask-marshmallow==0.14.0
- Flask-SQLAlchemy==2.5.1
- greenlet==1.1.3
- importlib-metadata==4.8.3
- importlib-resources==5.4.0
- itsdangerous==2.0.1
- Jinja2==3.0.3
- Mako==1.1.6
- MarkupSafe==2.0.1
- marshmallow==3.14.1
- marshmallow-sqlalchemy==0.27.0
- pkg_resources==0.0.0
- psycopg2==2.9.3
- psycopg2-binary==2.9.3
- PyJWT==2.4.0
- python-dotenv==0.20.0
- semantic-version==2.10.0
- setuptools-rust==1.1.2
- six==1.16.0
- SQLAlchemy==1.4.41
- typing_extensions==4.1.1
- urllib3==1.26.12
- Werkzeug==2.0.3
- zipp==3.6.0

<br>

## Entity Relationship Diagram for the API
![image](images/sprouterd.PNG)

<br>

## Project Model Relations
### User:
- Every user is identified by the primary key: user_id
- Every user has a 1-to-many relationship with The UserCategory and UserFeelingTable. Every User can create many user categories and user feelings.
- UserCategory and UserFeeling contain  the foreign key: user_id. 
- User categories and user feelings only have one user linked to them.

### UserCategory:
- Every user category is identified by the primary key: user_category_id.
- Every user category has a 1-to-many relationship with the UserActivity table. Every category can be linked to many user activities.
- UserActivity contains the foreign key: user_category_id.
- User activities can only have one category linked to them. Since each category can only have one user, each activity is only linked to one user.

### UserActivity:
- Every user activity is identified by the primary key: user_activity_id.
- Every user activity has a 1-to-1 relationship with the UserIcon table. Every activity can be linked to only one user icon.
- UserIcon contains the foreign key: user_activity_id.
- User icons can only have one user activity linked to them. Since each activity can only be linked to one category, and each category can only be linked to one user, each icon is only linked to one user.

### UserIcon:
- Every user icon is identified by the primary key: user_icon_id.
- The primary key for UserIcons is not featured in any other tables.
- UserIcon contains the foreign key: user_activity_id.

### UserFeeling:
- Every user feeling is identified by the primary key: user_feeling_id.
- Every user feeling has a 1-to-1 relationship with the UserFeelingIcon table. Every activity can be linked to only one user icon.
- UserFeelingIcon contains the foreign key: user_feeling_id.
- User feeling icons can only have one user feeling linked to them. Since each feeling  can only be linked to one user, each user feeling icon is only linked to one user.

### UserFeelingIcon:
- Every user feeling icon is identified by the primary key: user_feeling_icon_id.
- The primary key for UserFeelingIcon is not featured in any other tables.
- UserIcon contains the foreign key: user_feeling_id.

<br>

## Discuss the database relations to be implemented in your application

### Relations:
- <strong> User and UserCategory:</strong>

    The relationship between User and UserCategory is a 1-to-many-relationship. This means that each user can make many categories, but each category can only have one user associated with it. Users create categories to help structure their user activities in a user-friendly way.

- <strong>UserCategory and UserActivity:</strong>
- <strong>UserActivity and UserIcon:</strong>
- <strong>User and UserFeeling:</strong>
- <strong>UserFeeling and UserFeelingIcon:</strong>




<br>

## API Endpoints


<br>

### <strong>Endpoint: </strong>/user/register 
HTTP request verb: POST

Required data example:
```
{
    "user_name":"Frank",
    "user_email":"Frank@gmail.com",
    "user_password":"password"
}
```
Expected Response Example:
```
{
    "user_name": "Frank",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDYzMTQ1MCwianRpIjoiM2QzMjY1YjItZTZjMC00NTAxLTg3OTgtZjlhNmM0MDNjOTJlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE2NjQ2MzE0NTAsImV4cCI6MTY2NzIyMzQ1MH0.d93JLAINPCfSHTIEiInlkTD6nt3PrZVUlbrEGr3tTio"
}
```
---
<br>

### <strong>Endpoint: </strong>/user/login
HTTP request verb: POST

Required data example:

```
{
    "user_email":"Frank@gmail.com",
    "user_password":"password"
}
```
Expected Response Example:

```
{
    "user": "Frank",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDYzMTk1MCwianRpIjoiOTk3MjBjODEtZTU2Zi00ZmRkLTlkZGUtYzliMjczNjU1ZmM5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjMiLCJuYmYiOjE2NjQ2MzE5NTAsImV4cCI6MTY2NDcxODM1MH0.cBWn3D73NB0S4fdtvbuNP55LoOF0Xm2ZNNicPq1OP0s"
}
```
---

<br>

### <strong>Endpoint: </strong>/usercategory/create

HTTP request verb: POST

Authentication Requirement: User Token

Required data example:

```
{
    "user_category_name": "Work"
}
```
Expected Response Example One (If the user hasn't created that category yet):

```
{
    "user_category_name": "Work",
    "activities": [],
    "user_category_id": 7,
    "user_id": 1
}
```
Expected Response Example Two (If the user has created that category already):

```
{
    "error": "A category with that name already exists."
}
```
---

<br>

### <strong>Endpoint: </strong>/usercategory

HTTP request verb: GET

Authentication Requirement: User Token

Expected Response Example:
```
[
    {
        "user_category_name": "Activity",
        "user_category_id": 1
    },
    {
        "user_category_name": "Exercise",
        "user_category_id": 2
    },
    {
        "user_category_name": "Meal",
        "user_category_id": 3
    }
]
```

---

### <strong>Endpoint: </strong>/usercategory/<int:user_category_id>

HTTP request verb: PUT

Authentication Requirement: User Token

Required data example:

```
{
    "user_category_name": "Free Time"
}
```
Expected Response Example One (If the user hasn't used that category name yet):

```
{
    "user_category_name": "Free Time",
    "activities": [],
    "user_category_id": 1,
    "user_id": 1
}
```
Expected Response Example Two (If the user has used that category name already):

```
{
    "error": "A category with that name already exists."
}
```
---
<br>

### <strong>Endpoint: </strong>/usercategory/\<int:user_category_id>

HTTP request verb: DELETE

Authentication Requirement: User Token

Expected Response Example One (If user category exists):

```
{
    "message": "Category deleted successfully."
}
```

Expected Response Example Two (If user category doesn't exist):

```
{
    "error": "Category does not exist."
}
```
---

<br>

### <strong>Endpoint: </strong>/useractivity/\<int:user_category_id>/create

HTTP request verb: POST

Authentication Requirement: User Token

Required data example:

```
{
    "user_activity_name": "Swimming"
}
```

Expected Response Example One (If the user hasn't used that activity name yet):

```
{
    "user_activity_id": 9,
    "icons": null,
    "user_activity_name": "Swimming",
    "user_category_id": 3
}
```

Expected Response Example Two (If the user has used that activity name already):

```
{
    "error": "An activity with that name already exists."
}
```
---

<br>

### <strong>Endpoint: </strong>/useractivity/\<int:user_category_id>

HTTP request verb: GET

Authentication Requirement: User Token

Expected Response Example:
```
[
    {
        "user_activity_id": 3,
        "user_activity_name": "Lasagna"
    },
    {
        "user_activity_id": 9,
        "user_activity_name": "Swimming"
    }
]
```
---

<br>

### <strong>Endpoint: </strong>/useractivity/\<int:user_category_id>/\<int:activity_id>

HTTP request verb: PUT

Authentication Requirement: User Token

Required data example:

```
{
    "user_activity_name": "Jogging"
}
```
Expected Response Example 1 (If the user hasn't used that activity name yet):

```
{
    "user_activity_name": "Jogging",
    "user_activity_id": 9,
    "user_category_id": 3,
    "icons": null
}
```
Expected Response Example 2 (If the user has used that category name already):

```
{
    "error": "An activity with that name already exists."
}
```
---

<br>

### <strong>Endpoint: </strong>/useractivity/\<int:user_activity_id>

HTTP request verb: DELETE

Authentication Requirement: User Token

Expected Response One (If user activity exists):

```
{
    "message": "Activity deleted successfully."
}
```

Expected Response Two (If user activity doesn't exist):

```
{
    "error": "Activity does not exist."
}
```
---

<br>

### <strong>Endpoint: </strong>/usericon/<int:user_activity_id>/upload"

HTTP request verb: POST

Authentication Requirement: User Token

Required data example (image upload):

![image](images/uploadinput.PNG)

Expected Response Example One (If the activity did not have an associated image):

```
{
    "user_icon_id": 6,
    "user_icon_url": "http://res.cloudinary.com/dydrnv83j/image/upload/v1664635754/wd3nljxkp8cq6jpcgjlk.png"
}
```

Expected Response Example Two (If the activity did have an associated image):

```
{
    "error": "An image is already associated with this activity."
}
```
<br>

### <strong>Endpoint: </strong>/usericon/\<int:user_activity_id>

HTTP request verb: GET

Authentication Requirement: User Token

Expected Response Example:
```
[
    {
        "user_icon_id": 6,
        "user_icon_url": "http://res.cloudinary.com/dydrnv83j/image/upload/v1664635754/wd3nljxkp8cq6jpcgjlk.png"
    }
]
```
---

<br>

### <strong>Endpoint: </strong>/usericon/\<int:user_icon_id>

HTTP request verb: DELETE

Authentication Requirement: User Token

Expected Response One (If user icon exists):

```
{
    "message": "Image deleted successfully"
}
```

Expected Response Two (If user icon doesn't exist):

```
{
    "error": "Image does not exist"
}
```
---

<br>

### <strong>Endpoint: </strong>/userfeeling/create

HTTP request verb: POST

Authentication Requirement: User Token

Required data example:

```
{
    "user_feeling_name": "Frustrated"
}
```
Expected Response Example One (If the user hasn't created that feeling yet):

```
{
    "feeling_icon": [],
    "user_id": 1,
    "user_feeling_id": 8,
    "user_feeling_name": "Frustrated"
}
```
Expected Response Example Two (If the user has created that feeling already):

```
{
    "error": "A feeling with that name already exists."
}
```
---
<br>

### <strong>Endpoint: </strong>/userfeeling

HTTP request verb: GET

Authentication Requirement: User Token

Expected Response Example:
```
[
    {
        "user_feeling_id": 3,
        "user_feeling_name": "Angry"
    },
    {
        "user_feeling_id": 4,
        "user_feeling_name": "Tired"
    },
    {
        "user_feeling_id": 8,
        "user_feeling_name": "Frustrated"
    }
]
```
---

<br>

### <strong>Endpoint: </strong>/userfeeling/<int:user_feeling_id>

HTTP request verb: PUT

Authentication Requirement: User Token

Required data example:

```
{
    "user_feeling_name": "Excited"
}
```
Expected Response Example One (If the user hasn't used that feeling name yet):

```
{
    "user_id": 1,
    "feeling_icon": [],
    "user_feeling_name": "Excited",
    "user_feeling_id": 8
}
```
Expected Response Example Two (If the user has used that feeling name already):

```
{
    "error": "A feeling with that name already exists."
}
```
---

<br>

### <strong>Endpoint: </strong>/userfeeling/\<int:user_feeling_id>

HTTP request verb: DELETE

Authentication Requirement: User Token

Expected Response One (If user feeling exists):

```
{
    "message": "Feeling deleted successfully."
}
```

Expected Response Two (If user feeling doesn't exist):

```
{
    "error": "Feeling does not exist."
}
```
---

<br>

### <strong>Endpoint: </strong>/userfeelingicon/\<int:user_feeling_id>/upload
HTTP request verb: POST

Authentication Requirement: User Token

Required data example (image upload):

![image](images/uploadinput.PNG)

Expected Response Example One (If the feeling did not have an associated image):

```
{
    "user_feeling_icon_url": "http://res.cloudinary.com/dydrnv83j/image/upload/v1664637570/wwpjlrzqiqjx5apytfih.png",
    "user_feeling_icon_id": 7
}
```

Expected Response Example Two (If the feeling did have an associated image):

```
{
    "error": "An image is already associated with this feeling."
}
```
---

<br>

### <strong>Endpoint: </strong>/userfeelingicon/\<int:user_feeling_id>

HTTP request verb: GET

Authentication Requirement: User Token

Expected Response Example:
```
[
    {
        "user_feeling_icon_id": 8,
        "user_feeling_icon_url": "http://res.cloudinary.com/dydrnv83j/image/upload/v1664637716/zpbylhcztsgfqbli1hrg.png"
    }
]
```
---

<br>

### <strong>Endpoint: </strong>/userfeelingicon/\<int:user_feeling_icon_id>

HTTP request verb: DELETE

Authentication Requirement: User Token

Expected Response One (If feeling icon exists):

```
{
    "message": "Image deleted successfully"
}
```

Expected Response Two (If feeling icon doesn't exist):

```
{
    "error": "Image not found"
}
```
---


