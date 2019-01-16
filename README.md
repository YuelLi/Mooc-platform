# Mooc-platform
Django(2.1.2), MySQL(8.0) <br>
A project for self-study <br>
## An [Example](http://yuli1997.pythonanywhere.com/) of this project
## Get Started:
* Create virtual environment via venv:
* `python -m venv ENV`
* Create Mysql database
* Change Settings.py to configurate database
* Install required modules:
* `pip install -r requirements.txt`
* <strong>Be Noticed: </strong>
* This project is using mysql. You have to install [sqlclient for python](https://github.com/PyMySQL/mysqlclient-python).
* You also need to migrate models to database(after setting up database on settings.py):
* `python manage.py makemigrations`
* `python manage.py migrate`
* To use xamdin, you should create superuser:
* `python manage.py createsuperuser`
* Modify data on xadmin(localhost for example):
* http://localhost:8000/xadmin

## Logs:
* 10/29:
<br>Created virtual enviroment django_env and Django dev enviroment on Pycharm.
<br>MySQL database mooc_platform on localhost and installed [sqlclient for python](https://github.com/PyMySQL/mysqlclient-python).
* 11/05:
<br>Created 4 basic app:users, organization, courses, operation. operation is in the higher level that could import other apps .
* 11/07:
<br>Finished models.py in user and course. Started doing HTML/CSS files<br>
* 11/15:
<br>Finished models.py in organization and operaton.
<br>Found HTML/CSS templates online. 
* 11/24:
<br>Setting up using [xadmin](https://github.com/sshwsfc/xadmin) instead of default admin in Django.
<br>Started JS parts.
<br> Finished index.html and login.html
* 12/2:
<br> Finshing up xadmin Configuration on created models.
* 12/10:
<br> Finished index, login and register. For captach in register.html using [django-simple-captcha](https://github.com/mbi/django-simple-captcha)
* 12/14:
<br> Finished email verification
* 12/15:
<br> Reconfigured the set up
.....
* 1/7:
<br> Almost finished the project, host on pythonanywhere.com
<br> 
