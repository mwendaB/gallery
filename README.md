# The Gallary 
## Author  
  
>[mwendaB](https://github.com/mwendaB?tab=repositories)  
  
# Description  
This is a Django application gallery that allows a user to upload images for other to see and be able to to share by coping the image link.
  
##  Live Link  
 [View Site](https://bgallery.herokuapp.com/)  to visit the site
  
 
## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  
  

  
## Setup and Installation  
- the following are the procedure to follow to set up the project on your local matchine  
  
##### Cloning the repository:  
 ``` 
git clone https://github.com/mwendaB/gallery
```
##### Install and activate Virtual  
```
python3 -m venv --without-pip virtual
```

```
source virtual/bin/activate
```

```
curl https://bootstrap.pypa.io/get-pip.py | python
```
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```
python manage.py makemigrations
 ``` 
 Migrate  
 ```
 python manage.py migrate 
```
##### Run the application  
 ```
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8.9](https://www.python.org/)  
* [Django==3.2.9](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [brianmwenda255@gmail.com]  
  
## License 
[MIT](license)
* Copyright (c) 2021 **Brian Mwenda**