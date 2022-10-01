# Api Webserver Project
## Overview
This API provides data for a simple daily planner that has an intended audience of those with special needs/disabilities.  The API allows the user to create accounts through an email sign-up process.  Once signed up, the user can create categories for the types of tasks/acitivites they like to do on a daily basis.  After a category is created, the user can add activities to the category.  For example: The user creates a category named "Exercise" and adds "Swimming", "Jogging", and "Soccer."  Upon creation of an activity, the user will have the option of uploading an image to use as a visual representation of the activity.  This information is intended to be displayed in a user friendly interface that allows for the user to plan their day and act as a means of communication. Along with the create, read, update and delete ability of the daily planner comes a feature that allows the user to create feelings and assign visual representations of them.  This is intended to be displayed in a similar way as the activities, acting as a way for the user to communicate how they are currently feeling.

<br>

### Intended Use of Account Creation Features
---
![image](images/sproutimg.PNG)

<br>

### Intended Use of Category Creation and Editing Features
---
![image](images/sproutimg3.PNG)

<br>

### Intended Use of Category Creation and Editing Features
---
![image](images/sproutimg4.PNG)

<br>

### Intended Use of the Data Overall
---
![image](images/sproutimg2.PNG)

<br>


## Identification of the problem
---
The problem I am trying to solve with this application is the lack of a means for some with special needs/disabilities to communicate their feelings and how they want their day to be structured. During my time as a high school special needs teacher and  as a support worker, I've worked with countless individuals that are unable to communicate through speech, often needing visual help to communicate.  This application intends to provide a way for those who are unable to communicate verbally to gain autonomy by providing them a way to communicate their feelings, as well sa the structure of their day.

<br>

## Why it needs to be solved
---
This problem needs to be solved because far too many individuals are unable to communicate their feelings and wants verbally. After my time in the disabilities sector, I've noticed many individuals with disabilities are often times coasting through their days, doing what others want them to do because they are unable to communicate what they want and feel. This often leads to frustration and a feeling of helplessness. Everyone deserves a voice, and this API intends on facilitating that.

<br>

- Endpoint documentation should include
    - HTTP request verb
    - Required data where applicable
    - Expected response data
    - Authentication methods where applicable

<br>

<br>

## API Endpoints
---

<br>

### <strong>Endpoint: </strong>/user/register 
HTTP request verb: POST

Required data example:
```
{
    "user_name":"Frank",
    "user_email":"Frank@gmail",
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



<br>

## Entity Relationship Diagram for the API
![image](images/sprouterd.PNG)