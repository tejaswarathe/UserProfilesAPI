# UserProfilesAPI

# Cloning the project

Clone the repository in your local machine.

Open the terminal from the project directory.

Activate the virtual environ ment.

`$ source env/bin/activate`

Change directory to the outer Api directory and run the command.

`$ python manage.py runserver`

Visit the localhost link given in the terminal response.

# UserList
This API returns the list of all user profiles that has been created along with the profile pictures in 3 different sizes : small(100x100), large(200X200) and original.

**Request:**
-    url = 'http://localhost/users/'

    
**Response:**
```
[
    {
        "name": "Jeff",
        "picture": {
            "detailthumbnail": "http://localhost/users/profilepictures/656541116464.detailthumbnail.jpg",
            "listthumbnail": "http://localhost/users/profilepictures/656541116464.listthumbnail.jpg",
            "original": "http://localhost/users/profilepictures/656541116464.jpg"
        }
    },
    {
        "name": "Betty",
        "picture": {
            "detailthumbnail": "http://localhost/users/profilepictures/6000195494285_R.detailthumbnail.jpg",
            "listthumbnail": "http://localhost/users/profilepictures/6000195494285_R.listthumbnail.jpg",
            "original": "http://localhost/users/profilepictures/6000195494285_R.jpg"
        }
    }
]
```

# UserDetail
This API return a single object in JSON format which includes a name and profile pictures in 3 sizes.

**Request:**
-    url = 'http://localhost/users/name'

**Response:**
```
{
    "name": "Jeff",
    "picture": {
        "detailthumbnail": "http://localhost/users/profilepictures/656541116464.detailthumbnail.jpg",
        "listthumbnail": "http://localhost/users/profilepictures/656541116464.listthumbnail.jpg",
        "original": "http://localhost/users/profilepictures/656541116464.jpg"
    }
}
```


# UserCreate
This API creates a new user and gives a POST request to the server creating a new user.

 **Request:**
-    url = 'http://localhost/users/create/'

 **Parameters:**

-   name
-   image_upload
