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

## Task Allocation and Tracking
### Overview

<strong>Trello Link:</strong> https://trello.com/b/Uvv1FNzD/sprout-planner

Task allocation and tracking were done through the use of the online tool Trello.  Tasks were organized by the columns "To-do", "Doing", and "Done". Tasks were assigned due dates based on the need for completion. For instance, all planning tasks were given quicker deadlines than coding tasks. Each task was assigned a label to signify what kind of task it is.  Setup tasks were given green labels with the word "Setup" inside.  Coding tasks were given a yellow label with the word "Coding" inside. Finalization tasks were given an orange label with the word "Finalization" inside.  The order of completion was the following: Setup, Coding, then Finalization. Within these task are checklists that must be completed before the task can be moved to the "Done" column. When a task is begun, the task would be moved to the "Doing" column.  When a task is completed it would be moved to the "Done" column. If code in one of the completed tasks broke or a new idea needed to be implemented, the related task would be moved back to the "Doing" column. 

<strong>Full Trello Board:</strong>

![image](images/trello.PNG)

<strong>Trello Task:</strong>

![image](images/routechecklist.PNG)

<br>

## Chosen Database System

The database system used for this API is PostgreSQL.  PostgreSQL is an open source object-relational database system that utilizes the SQL language.  I chose PostgreSQL due to it's track record  of being scalable, secure, and ensuring data integrity. PostgreSQL is also beginner friendly. Since this is my first API, that played a large role in choosing it. 

Despite the benefits, their are some drawbacks to choosing PostgreSQL.  In regards to performance, PostgreSQL is slower than competitors such as MySQL. PostgreSQL places compatibility at the top of it's list, so changes for improvements in speed are more involved than its competitors. Overall, I found PostgreSQL easy to work with despite being rather green in the API world.

<br>

## Key functionalities and Benefits of an ORM
Object-Relational-Mapping is a technique for writing queries using the object-oriented paradigm preferred by the developer. For instance, in the case of SQL, a typical query would look something like this:

```
SELECT customers.id 
AS customers_id, customers.name 
AS customers_name, customers.address 
AS customers_address, customers.email 
AS customers_email
FROM customers
```

Object-relational-mappers allow for this same query to be created using the preferred language of the developer. Typically, when the word ORM is used, it is referring to the library that facilitates this technique. Below is an example of the same query from above written for a Python Flask application using SQLAlchemy.

```
result = session.query(Customers).all()
```

### Benefits
- Ability to utilize the language that the developer is familiar with or already using for the project.
- ORMs are jam packed with powerful features such as support migrations and seeding.
- Queries written using ORM are often perform much better than programmer written SQL statements. 
- You can use an ORM without have much to any SQL knowledge.
- Improves the maintainability of your code.
- Most importantly, it speeds up the development process which reduces development time and costs.

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
- Every user has a one-to-many relationship with The UserCategory and UserFeelingTable. Every User can create many user categories and user feelings.
- UserCategory and UserFeeling contain  the foreign key: user_id. 
- User categories and user feelings only have one user linked to them.

### UserCategory:
- Every user category is identified by the primary key: user_category_id.
- Every user category has a one-to-many relationship with the UserActivity table. Every category can be linked to many user activities.
- UserActivity contains the foreign key: user_category_id.
- User activities can only have one category linked to them. Since each category can only have one user, each activity is only linked to one user.

### UserActivity:
- Every user activity is identified by the primary key: user_activity_id.
- Every user activity has a one-to-one relationship with the UserIcon table. Every activity can be linked to only one user icon.
- UserIcon contains the foreign key: user_activity_id.
- User icons can only have one user activity linked to them. Since each activity can only be linked to one category, and each category can only be linked to one user, each icon is only linked to one user.

### UserIcon:
- Every user icon is identified by the primary key: user_icon_id.
- The primary key for UserIcons is not featured in any other tables.
- UserIcon contains the foreign key: user_activity_id.

### UserFeeling:
- Every user feeling is identified by the primary key: user_feeling_id.
- Every user feeling has a one-to-one relationship with the UserFeelingIcon table. Every activity can be linked to only one user icon.
- UserFeelingIcon contains the foreign key: user_feeling_id.
- User feeling icons can only have one user feeling linked to them. Since each feeling  can only be linked to one user, each user feeling icon is only linked to one user.

### UserFeelingIcon:
- Every user feeling icon is identified by the primary key: user_feeling_icon_id.
- The primary key for UserFeelingIcon is not featured in any other tables.
- UserIcon contains the foreign key: user_feeling_id.

<br>

## Discuss the database relations to be implemented in your application
*Relations are available visually in the ERD section above.*

### Relationships:
- <strong> User and UserCategory:</strong>

    The relationship between User and UserCategory is a one-to-many-relationship. This means that each user can make many categories, but each category can only have one user associated with it. This is achieved by using the primary key from User as a foreign key in UserCategory. Users are able to see, modify, and delete only the categories that they have created. Users are meant to create categories to help structure their user activities in a user-friendly way.

<br>

- <strong>UserCategory and UserActivity:</strong>

    The relationship between UserCategory and UserActivity is a one-to-many relationship. This means that each category can contain many activities, but each activity can only have one parent category. This is achieved by using the primary key from UserCategory as a foreign key in UserActivity. Since each category is only attached to one user and each activity is only attached to one category, that means that each activity is only attached to one user as well. If a category is deleted by a user, all associated activities will be deleted as well.

<br>

- <strong>UserActivity and UserIcon:</strong>

    The relationship between UserActivity and UserIcon is a one-to-one relationship.  This means that each activity is associated with one just one icon, and the same is true for the reverse. This is achieved by using the primary key in UserActivity as the foreign key in UserIcon.  Since each icon is only attached to one activity, which is only attached to one category, which is only attached to one user,  each icon is only attached to one user.  If any of the user icons parents are deleted by the user, the user icon will be deleted as well. 
    
<br>

- <strong>User and UserFeeling:</strong>
     The relationship between User and UserFeeling is a one-to-many-relationship. This means that each user can make many feelings, but each feeling can only have one user associated with it. This is achieved by using the primary key from User as a foreign key in UserFeeling. Users are able to see, modify, and delete only the feelings that they have created. 
<br>

- <strong>UserFeeling and UserFeelingIcon:</strong>
    The relationship between UserFeeling and UserFeelingIcon is a one-to-one relationship.  This means that each feeling is associated with one just one feeling icon, and the same is true for the reverse. This is achieved by using the primary key in UserFeeling as the foreign key in UserFeelingIcon.  Since each feeling icon is only attached to one feeling, which is only attached to one user, each feeling icon is only attached to one user. If the feeling associated with a feeling icon is deleted, the feeling icon will be deleted as well.

<br>




## API Endpoints


<br>

### <strong>Endpoint: </strong>/user/register 
HTTP Request Verb: POST

Required Data Example:
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
HTTP Request Verb: POST

Required Data Example:

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

HTTP Request Verb: POST

Authentication Requirement: Token generated on login

Required Data Example:

```
{
    "user_category_name": "Work"
}
```
Expected Response Example One (If the user hasn't created that category yet):

```
{
    "user_category_name": "Work",
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

HTTP Request Verb: GET

Authentication Requirement: Token generated on login

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

HTTP Request Verb: PUT

Authentication Requirement: Token generated on login

Required Data Example:

```
{
    "user_category_name": "Free Time"
}
```
Expected Response Example One (If the user hasn't used that category name yet):

```
{
    "user_category_name": "Free Time",
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

HTTP Request Verb: DELETE

Authentication Requirement: Token generated on login

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

HTTP Request Verb: POST

Authentication Requirement: Token generated on login

Required Data Example:

```
{
    "user_activity_name": "Swimming"
}
```

Expected Response Example One (If the user hasn't used that activity name yet):

```
{
    "user_activity_id": 9,
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

HTTP Request Verb: GET

Authentication Requirement: Token generated on login

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

HTTP Request Verb: PUT

Authentication Requirement: Token generated on login

Required Data Example:

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

HTTP Request Verb: DELETE

Authentication Requirement: Token generated on login

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

HTTP Request Verb: POST

Authentication Requirement: Token generated on login

Required Data Example (image upload):

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

HTTP Request Verb: GET

Authentication Requirement: Token generated on login

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

HTTP Request Verb: DELETE

Authentication Requirement: Token generated on login

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

HTTP Request Verb: POST

Authentication Requirement: Token generated on login

Required Data Example:

```
{
    "user_feeling_name": "Frustrated"
}
```
Expected Response Example One (If the user hasn't created that feeling yet):

```
{
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

HTTP Request Verb: GET

Authentication Requirement: Token generated on login

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

HTTP Request Verb: PUT

Authentication Requirement: Token generated on login

Required Data Example:

```
{
    "user_feeling_name": "Excited"
}
```
Expected Response Example One (If the user hasn't used that feeling name yet):

```
{
    "user_id": 1,
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

HTTP Request Verb: DELETE

Authentication Requirement: Token generated on login

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
HTTP Request Verb: POST

Authentication Requirement: Token generated on login

Required Data Example (image upload):

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

HTTP Request Verb: GET

Authentication Requirement: Token generated on login

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

HTTP Request Verb: DELETE

Authentication Requirement: Token generated on login

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


