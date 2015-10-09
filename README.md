P1
A Movie Trailer Website where users can see A list of movies and watch the trailers. Website stores a list of movie titles, box art, poster images, and movie trailer URLs. The data will then be expressed on the web page and allow users to review the movies and watch the trailers. Users can also add their favorite movie to the list by filling a webform.

Structure
p1/
├── manage.py
├── db.sqlite3
├── .gitignore.swp
├── .README.md
├── movie_list/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── p1/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
	 └── templates/
	    ├── index.html
	 └── migration/
		├── __init__.py
		├── 0001_initial.py
Installation

To install this app you need to have the following prerequests first:
-Python environment running on your machine (windows,mac,linux) if you do not have python installed please search (python download) using your favorite search engine and folllow the instructions
-You will also need to download django. 
if you have all your python enivronment setup correctily you should be able to run "pip install Django==1.8.5"
-Not Sure what django is?
You can visit https://www.djangoproject.com/start/overview/ for more Info and instructions on how to setup django
-Download the app and extract the directory where you can run python and django commands
-Make sure you are in the directory where "manage.py" is located open a terminal window and type "manage.py runserver"
this will prompted django to run a server on your localhost at port 8000 usually.
-Make sure the port that django specifies is not being used by other applications
-Navigate to localhost:8000/p1 on your favorite web browser and you should see the app running
- If you wish to interact with the database directly go to localhost:8000/admin you should be greeted with a login use "udacity" as username "udacity" as password
you will find info table that holds all the movie objects created. Objects are referenced by movie title.


License
Code released under the MIT license. 

