# DjangoEventScheduler_Day2
To create project- django-admin startproject project_name.
To start server- python manage.py runserver.
views.py file contain functions that take http request and generate output.
create template folder same path like manage.py file and inside template folder create html files.
urls.py file we import views,path and it contain urls of each html page.
manage.py containg all backround information.
In models.py, we create model of index, name,date,time,description of event with proper datatype.
database used is sqlite3.
For reflecting data to the database first do migration then migrate.
for migration-python manage.py makemigrations.
for migrate-pyton manage.py migrate.


