# Django_Introduction_login_register
<img class="alignnone size-full wp-image-84" src="https://getpython.files.wordpress.com/2019/05/django_basic_login.png" alt="Django_basic_login" width="800" height="600" />
<h3>How to run this app:</h3>
<ul>
	<li>clone this repository</li>
	<li>Install requirement file</li>
	<li>open directory where manage.py file is present</li>
	<li>open terminal  type the following command
<pre>pip3 install -r requirement.txt
python3 manage.py runserver</pre>
</li>
</ul>
<h3></h3>
<h3>What is Django :</h3>
Django is a web development framework of python programming language. As we all know that Python programming language is not less than a treasure to a developer. It offers an abundance of libraries, packages, and framework. Django is one of them, it was developed for newspaper website so website development is easy. Django follows the Model Template View (MTV) architecture which makes it very secure. Surprisingly websites of famous organizations such as NASA, Instagram, Pinterest, and Bitbucket are developed in Django.
<h3>How to install Django :</h3>
<div></div>
open your terminal and paste this command
<pre><span id="pip-command">pip install Django</span></pre>
<h3>How to start your project:</h3>
<pre>django-admin startproject myproject</pre>
<img class="alignnone size-full wp-image-85" src="https://getpython.files.wordpress.com/2019/05/screenshot-from-2019-05-27-22-00-00.png" alt="Screenshot from 2019-05-27 22-00-00" width="655" height="386" />

Now you can see we have created a project folder using the above command. these files created in the root directory of your project.

Manage.py file plays a very significant role in whole Django development, it helps to run the project, create superuser and many more we will talk about it later

<img class="alignnone size-full wp-image-92" src="https://getpython.files.wordpress.com/2019/05/screenshot-from-2019-05-30-01-09-44.png" alt="Screenshot from 2019-05-30 01-09-44" width="940" height="278" />

this is the subdirectory of the project folder, here I explain you the significance of each file
<ul>
	<li>The __init__.py file is a blank file, basically, it represents folder as a package</li>
	<li>settings.py  file contains the whole configuration of the Django file</li>
	<li>URLs.py file is used to establish a path between views and template</li>
	<li>wsgi.py file is used for app deployment on server.</li>
</ul>
Now this is all for the project folder lets move to the app section
<h3>How to create an app for your project:</h3>
First, go to the root directory and type the following command
<pre>django-admin startapp myapp</pre>
<img class="alignnone size-full wp-image-91" src="https://getpython.files.wordpress.com/2019/05/screenshot-from-2019-05-30-01-08-35.png" alt="Screenshot from 2019-05-30 01-08-35.png" width="952" height="332" />

Now you can see our app folder created, open it and check the significance of each file

<img class="alignnone size-full wp-image-93" src="https://getpython.files.wordpress.com/2019/05/screenshot-from-2019-05-30-01-11-18.png" alt="Screenshot from 2019-05-30 01-11-18" width="1212" height="342" />

This is an app folder, here I will show you the functionality of important files
<ul>
	<li>views.py file which is responsible for whole functionality, In this file we write our function and render them on a specific HTML page.</li>
	<li>models.py file where we can specify our database structure using the class-based approach. Here we can make tables, create relation on the basis of ORM.</li>
	<li>the admin.py file acts as a waiter between models and admin panel. It just makes the connection so that we can see our tables data in the admin panel</li>
</ul>
<h3></h3>
<h3>Now  configure settings,py file:</h3>
<h4>step 1: Register your app in Django installed an app</h4>
<img class="alignnone size-full wp-image-89" src="https://getpython.files.wordpress.com/2019/05/screenshot-from-2019-05-30-01-00-40.png" alt="Screenshot from 2019-05-30 01-00-40" width="844" height="470" />
<h3>step 2: Mention static Directory and templates path details</h3>
Create two folders in the root directory
<ul>
	<li>static: it will contain our static files such as images, CSS and js</li>
	<li>templates: this folder contains our HTML files for our app</li>
</ul>
<img class="alignnone size-full wp-image-94" src="https://getpython.files.wordpress.com/2019/05/screenshot-from-2019-05-30-01-14-38.png" alt="Screenshot from 2019-05-30 01-14-38.png" width="1138" height="233" />

I hope your root directory looks as described in the above picture

<img class="alignnone size-full wp-image-90" src="https://getpython.files.wordpress.com/2019/05/screenshot-from-2019-05-30-01-04-34.png" alt="Screenshot from 2019-05-30 01-04-34" width="1008" height="429" />

In this picture, I have concatenated root directory of the project with static folder

<img class="alignnone size-full wp-image-95" src="https://getpython.files.wordpress.com/2019/05/screenshot-from-2019-05-30-01-04-50.png" alt="Screenshot from 2019-05-30 01-04-50" width="1160" height="580" />

In this step, I have initialized templates folder so that our Django can easily locate it.

<img class="alignnone size-full wp-image-96" src="https://getpython.files.wordpress.com/2019/05/screenshot-from-2019-05-30-01-05-28.png" alt="Screenshot from 2019-05-30 01-05-28" width="1277" height="695" />

Here I have mentioned static files directory, It will use a lot of time in this project
<h3>Understand the functionality of MTV structure:</h3>
First understand what views.py fille does, basically it a python file which works on function here one can make function according to his own desire. Every function returns its response to the front end (HTML pages) with dynamic data.

For example, let's say we have a views.py file and have a function name demo which returns its data into an HTML page name demo.html (all HTML files should in a static folder).

views.py
<pre>def demo(request):
    username = "rajat"
    context = {
    'name': username
    }
    return render(request,'demo.html',context)</pre>
<h3>I hope you understood the functionality of views.py file, now open the HTML file and call data using Jinja2 (The Python Template Engine)</h3>
 

jinja 2 template call variable data in {{}} format, it also use flow control as well as conditional statements using {}.

Now open demo.html file
```<!DOCTYPE html>
{% load staticfiles %}
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <h1>User name is : {{name}}</h1>
  </body>
</html>
```
Now our function, HTML page are ready now we need to create a separate URL for this HTML page so we need to edit urls.py of our project.

urls.py
<pre>from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.demo, name = 'demo'),
    ]</pre>
Here I just configured its URL path I put empty string because I want it landing page. Suppose one just one to name it as Path('demo', views.demo) then one should open this page like this  http://127.0.0.1:8000/demo.
<h2>How to create Super User in Django:</h2>
enter this command on your project root directory
<pre>python3 manage.py createsuperuser</pre>
 

this command created your superuser now one can run the local server and view the admin panel
<pre>python3 manage.py runserver</pre>
<h1><img class="alignnone size-full wp-image-97" src="https://getpython.files.wordpress.com/2019/06/screenshot-from-2019-06-03-00-08-11.png" alt="Screenshot from 2019-06-03 00-08-11.png" width="1299" height="659" /></h1>

Thank you for reading this article
