# DjangoRestFramework
Created Rest apis with Django Rest framework to implement my understanding and to get some experience.
in urls.py it is always better to put a / in the end like 'rental_review/'
urlpatterns = [
    path('rental_review/',views.rental_review,name='rental_review'),
    path('thank_you/',views.thank_you,name='thank_you')

]



project is also called as site/website

its better to have names like my_site and my_app

Most of the pages are working on 8080 port only python manage.py runserver 8080



open cmd as admin then goto desired location
using the django admin tool we can easily get the directory structure 

if django was installed in a virtual environment activate it first
i used >python -m django startproject FirstProject 
as django-admin startproject mysite didnt work
with django-admin u can call many commands


in the terminal in Vs Code when u open terminal Powershell opens beside the name towards right below there will be 
+ symbol click n that and change to Comand prompt

now goto the directory containinf the manage.py and run the command
python manage.py runserver
python manage.py runserver 8080 # to run on 8080 port

we can have different functionality like photo s as part of a project and all these functionality is considered as a separate app.
to start a app from project u do 
python manage.py startapp <appname>

FirstApp is created.'
in views.py import Http Response and write a function index that returns a response
create a urls.py folder in FirstApp add the import views lines and
and add path to urlpatterns list

next goto urls.py in FirstDjangoProject and add the url there as well.

start the server as python manage.py runserver
and goto http://127.0.0.1:8000/firstapp/ u should see output from views.py

FirstProject is also called as Website
and FirstApp is called as App


Now to modify thehome page in the Project directory add Views.py
add home function there
next in urls.py in FirstDjangoProject add a path line for the home function in views.py


# in FirstApp/urls.py it is of type Function Views
#    in FirstProject/urls.py  path('firstapp/',include('FirstApp.urls')), is of type  URLconf 
#     path('firstapp/',include('FirstApp.urls')) neeeds to be added only once 
# once added it links firstapp/ to urls in firstapp.urls 
# next for example if u have  path('abc ',views.index) in FirstApp/urls then that can be acceses as
# /firstapp/abc


next see secondApp views.py and urls.py ..for dynamic views and url patterns]
https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters


ThirdApp is about Templates
connecting url to views and then to templates
First add url in urls.py in ThirdApp
Also add that url to the urls.py in project/website level
next create a view that renders
create a folder called templates in the diredctry containing manage.py ie template is at the project level
create another folder that matches the app name ThirdApp and in that create example.html
and add thirdapp/exmaple.html in render in the view

now start the server 
hit http://127.0.0.1:8000/thirdapp/ it gives error as 
TemplateDoesNotExist at /thirdapp/
Third_App/example.html


Template-loader postmortem
Django tried loading these templates, in this order:

Using engine django:

django.template.loaders.app_directories.Loader: C:\Users\Student\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\django\contrib\admin\templates\Third_App\example.html (Source does not exist)
django.template.loaders.app_directories.Loader: C:\Users\Student\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\django\contrib\auth\templates\Third_App\example.html (Source does not exist)


So we have tell Django to look for my template

if u goto Settings.py there is INstalled_apps 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',

that list doesnt ahve my firstapp, secondapp, thirdapp,.. we have to use migrations and install that application

there is also section for templatesTEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,


django by default looks for templates in BACKEND but we can give our own in DIRS
EVENTUALLY we will be using 'APP_DIRS': True, which means to look for templates in out APP_DIRS
but currently we dont have our app in installed apps section 



django takes DIRS and tells to look for templates in those directories
but to do that we have to import OS

there is a line # Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent which automatically builds out whats knows as base directorty
and we can use that to join our templates folder.
so import OS 
and in 'DIRS': [os.path.join(BASE_DIR,templates/)],



From now on we are going to create templates directory in the app itself
we r going to use more templates and od migration as well this time 
and follow the directory structure of 08-Django-and-templates pg 18
this time we are createing templeates folder under app
creating a new project as well this time
SecondProject
>python -m django startproject SecondProject

Step 1 for creating a new app
python manage.py startapp FirstApp
create urls.py in FirstApp
only create urls and views.py
Dont create templates directorys

in the cmd python manage.py migrate
now have a look at apps.py in FirstApp
its is like 
class FirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FirstApp'

Now in settings.py add the line  chnage
INSTALLED_APPS = [
    'FirstApp.apps.FirstappConfig',


Now run python manage.py makemigrations FirstApp

C:\Users\Student\Desktop\Untitled Folder\Python\SecondProject>python manage.py makemigrations FirstApp
No changes detected in app 'FirstApp'

Now create the folder templates -- cereate FirstApp under that now
example.html
Step 2 -- from step 1 to here for creating a new app
variable.html is for passing the context from the view to html
in view we created a dictionary and passed that in contexti
in html refere it wish 2 {{}}

Now in marketplace install Django extension 
later u can disable it as it conflicts wiyh some of html auto complete.
Now if u see variable.html file the code will have different colours to differentiate html and django code

in variable.html ---{{first_name | upper}} upper is the filter


Django Tags
in html are {% %}



SecondApp is about creating tags ad url names in Templates
having a link for variable.html in example.html
create the secondApp and Follow Step 1 for creating a new app till step 2
and now we have example.html, variable.hyml and views.py and urls.py

create a variable called app_name in urls.py
next gives names for url patterns
Nowmake changes in example.html as 
  url 'SecondApp:variable'  is for a url on SecondApp 
        <br> if u have a url on the project level like any home page and u have view for that on the project level
        <br> u can reference that by just variable without the appname

SecondApp is about Template Inheritance
myapp:abse.html for base.html inside myapp
in here we are inheriting the base.html at project level in to differenet apps
as we are referring templates ar project level we have to import os and add dirs IN settings.py
at the project level created templates folder and base.html
in SecondApp - templates add inheritance.html
next added it to settings DIRS by importing OS
also add a view for inheritance.html



Next we are creating a custom 404 error page.
as the error page should be common for all the apps , the error page should be under the project templates
under the porject/templates create 404.html ----- in next steps i changed this name to error_view.html
in the url if u just give abcd it gives a page not found as debug=True
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/secondapp/sports
Using the URLconf defined in SecondProject.urls, Django tried these URL pat

in settings.py set debug=false
and 
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

now if u hit http://127.0.0.1:8000/secondapp/abcd 
like in place of abcd u can give anything that is not yet implemented
it shows the 404.html
the file name should be 404.html only as DJango has a 
404.html and u r overriding it

but lets see how to use some other name --rename 404.html to error_view.html
we can achieve it using views
in priject level create views.py and
function name can be anything but we are matching the documentaions
# frunction name can be anything but lets macth with the name in documentation 
# along with request it has exception as the 2nd argument
def my_custom_page_not_found_view(request,exception):


and in urls.py in project level 
add handler404 = "SecondProject.views.my_custom_page_not_found_view"



Static files:
like .cc, .js, .jpeg
instead pf using the full path u can use {%static%}
For now keep the image in the folder wehere manage.py is present 
ie at the project level later we will move this to some static folder.
in settings.py  verify django.contrib.staticfiles  in installed_apps

there is a line STATIC_URL = 'static/' it is ok for now
later if we move the static files to some folder. we have to modify this similar to myapp/static/myapp similar to templates
as we have 'static/' here
create static/second_app under second_app and move the jpeg file here SK.jpg
create image.html in templates and create a view for it  image_static_view and update url similar to example.html or variable.html
in image.html add {% load static%} to load static directory with {%load static%}
and <img src="{% static 'SecondApp/sk.jpg'%}" alt="my image">

manage.py runserver --insecure works for serving static files with debug=True
With debug turned off Django won't handle static files for you any more - your production web server (Apache or something) should take care of that.



Read 09 file in Django folder on mobile
ThirdProject:
Models:
=======
open cmd as admin then goto desired location
using the django admin tool we can easily get the directory structure 

if django was installed in a virtual environment activate it first
i used >python -m django startproject ThirdProject 
python manage.py startapp FirstApp

goto settings.py and there u will see 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Django knows that as we are using django that means we have python
sqlite3 comes with python so Django makes sqlite3 default

Steps on connecting to other databases is at :
https://docs.djangoproject.com/en/4.1/ref/settings/#databases

When connecting to other database backends, such as MariaDB, MySQL, Oracle, or PostgreSQL, additional connection parameters will be required. See the ENGINE setting below on how to specify other database types. This example is for PostgreSQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

Search for databases in Django search bar:
https://docs.djangoproject.com/en/4.1/ref/databases/

3rd party databases: https://docs.djangoproject.com/en/4.1/ref/databases/#third-party-notes


there is DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} in settings.py but we dont see any sqlite3 
once we run migrate command we will see that
python manage.py migrate
it createss dqlite3 and also looks at the installed apps inside settings.py and creates any necessary database tables.

lets goto models.py
each class inside models.py represents a table and each field representa  column
lets create Patient class and it inheirts from model.Model

https://docs.djangoproject.com/en/4.1/ref/models/fields/
# IN ABOVE URL we ahave all field details

we have fields like autoNow --- to automatically fill current time absed on button click
charfield, integerfield
there are some validations also like MinValueValidator, maxValueValidator in the same page

while writing models.CharField, integerField we have autosuggestions as we hafve enabled the django extension
just created patient class and saved the changes for now.

For migrations to work we have to add to installed apps in settings.py

now have a look at apps.py in FirstApp
its is like 
class FirstappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FirstApp'

Now in settings.py add the line  chnage
INSTALLED_APPS = [
    'FirstApp.apps.FirstappConfig',


Now run python manage.py makemigrations FirstApp
Now under migrations there will be 0001_initial.py
this is the python file created by Django which wil eventually create the actual sequel code in order to interact with the db
u can mess with this and make modifications
there is fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),

id is  primary key  field. 

to see the actual sql code u can run 
python manage.py sqlmigrate firstapp 0001  <0001 here is 0001_initial.py>
the output of this is
python manage.py sqlmigrate FirstApp 0001      
BEGIN;
--
-- Create model Patient
--
CREATE TABLE "FirstApp_patient" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "age" integer NOT NULL);     
COMMIT;


To make the actual changes do python manage.py migrate

Data creation and insertion
==========
can be done in 3 ways
create object and save
objects.create()
objects.bulk_create()



1st way:
=========
lets create an object from command line first
(terminal lshould always be command promot
by default when u open terminal it opens powershell , towards right botton beside the name
there will be + symbol click on that and select command prompt )
python manage.py shell 
import Paitent Using
from FirstApp.models import Patient
carl = Patient(first_name='carl',last_name='smith',age=30)
carl.age   --print age back)

we have only created the object we have not saved yet
carl.save()


.save method came from the inherited models.Model class


2nd way:
=========
Patient.objects.create(first_name='susan',last_name='smith',age=40)
output is <Patient: Patient object (2)>
it refelect the index position

3rd way
=====
https://docs.djangoproject.com/en/4.1/ref/models/querysets/#bulk-create
there are some caveats with this method
main drawback is this query doesnt work with many to many relations

(generally only 1 query, no matter how many objects there are),  if there are too many records
wwe canuse batch size to fix.

myList=[Patient(first_name='adam',last_name='smith',age=40),Patient(first_name='karl',last_name='marx',age=40)]

Patient.objects.bulk_create(myList)
returns output as [<Patient: Patient object (3)>, <Patient: Patient object (4)>]


many sample queries :
https://docs.djangoproject.com/en/4.1/topics/db/queries/

Fetching the data from DB:
==================
start the python shell using python manage.py shell
from FirstApp.models import Patient

Patient.objects.all() returns the queryset

<QuerySet [<Patient: Patient object 
(1)>, <Patient: Patient object (2)>, <Patient: Patient object (3)>, <Patient: Patient object (4)>]>

>>> Patient.objects.all()[0] 
<Patient: Patient object (1)>

It is returning the data like that becoz in our model we dont have __str__method to view theobject
lets define __str__ method
def __str__(self):
        return f"{self.first_name} and {self.last_name} his age = {self.age}"


we have to quit() and restaert the shell with python manage.py shell to register the changes.

we have to import Patient again for it to work.

>>> Patient.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Patient' is not defined
>>> from FirstApp.models import Patient
>>> Patient.objects.all()
<QuerySet [<Patient: carl and smith his age = 30>, <Patient: susan and smith his age = 40>, <Patient: adam and smith his 
age = 40>, <Patient: karl and marx his age = 40>]>


Filter and get
============
get allows us to grab one single item 
if multiple rows are present for search criteriea it throws an error
like based on primary key 
we can use filter to further narrow down our results and also to return multiple records and it returns a queryset
.get()
.filter()
operators..and and or


>>> Patient.objects.get(pk=1)
<Patient: carl and smith his age = 30>
>>> Patient.objects.get(first_name='carl')
<Patient: carl and smith his age = 30>
>>> Patient.objects.get(last_name='smith')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\Student\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\django\db\models\manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\Student\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\django\db\models\query.py", line 653, in get
    raise self.model.MultipleObjectsReturned(
FirstApp.models.Patient.MultipleObjectsReturned: get() returned more than one Patient -- it returned 3!


>>> Patient.objects.get(first_name='smith')
Traceback (most recent call last):  File "<console>", line 1, in <module>
  File "C:\Users\Student\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\django\db\models\manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)      
  File "C:\Users\Student\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\django\db\models\query.py", line 650, in get
    raise self.model.DoesNotExist(FirstApp.models.Patient.DoesNotExist: Patient matching query does not exist.


.filter()
============
>>> Patient.objects.filter(last_name='smith').all()
<QuerySet [<Patient: carl and smith his age = 30>, <Patient: susan and smith his age = 40>, <Patient: 
adam and smith his age = 40>]>  
>>> Patient.objects.filter(last_name='smith').filter(age=40).all()  
<QuerySet [<Patient: susan and smith his age = 40>, <Patient: adam and smith his age = 40>]>


operators()
================
https://docs.djangoproject.com/en/4.1/ref/models/querysets/#q-objects

from django.db.models import Q
>>> Patient.objects.filter(Q(last_name='smith') & Q(age=40)).all()
<QuerySet [<Patient: susan and smith his age = 40>, <Patient: adam and smith his age = 40>]>



For more complex operations we use field lookups with a filter call.
Model.objects.filter(name__startswith="S")

fieldname(2_)operator

>>> Patient.objects.filter(last_name__startswith="S").all()
<QuerySet [<Patient: carl and smith 
his age = 30>, <Patient: susan and smith his age = 40>, <Patient: adam and smith his age = 40>]>

>>> Patient.objects.filter(age__in=[30,40]).all()
<QuerySet [<Patient: carl and smith 
his age = 30>, <Patient: susan and smith his age = 40>, <Patient: adam and smith his age = 40>, <Patient: karl and marx his age = 40>]>


>>> Patient.objects.filter(age__gte=39).all()
<QuerySet [<Patient: susan and smith his age = 40>, <Patient: adam and smith his age = 40>, <Patient: karl and marx his age = 40>]>
even for gte u use =



https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups

better read all https://docs.djangoproject.com/en/4.1/ref/models/querysets/#queryset-api-reference


>>> Patient.objects.order_by('age').all()
<QuerySet [<Patient: carl and smith 
his age = 30>, <Patient: susan and smith his age = 40>, <Patient: adam and smith his age = 40>, <Patient: karl and marx his age = 40>]>



updating models:
============
there wilwl be a time when u want to add new fields.
2 options:
1) choose a defaults value on the spot when making the migratoins file
2) cancel the migrations and create a default value within the model 


lets add a new field  heartrate to Patient
    heartrate = models.IntegerField()

save 

C:\Users\Student\Desktop\Untitled Folder\Python\ThirdProject>python manage.py makemigrations FirstApp
It is impossible to add a non-nullable field 'heartrate' to patient without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option: 2

C:\Users\Student\Desktop\Untitled Folder\Python\ThirdProject>

its better to provide default values in models.py
 so modify the heartrate as 
    heartrate = models.IntegerField(default=60)
or
    heartrate = models.IntegerField(null=True)

for now we are going with default = 60

lets make some validations for age and heartrate

https://docs.djangoproject.com/en/4.1/ref/validators/
from django.core.validators import MaxValueValidator,MinValueValidator

change     age  = models.IntegerField()
 to 
    age  = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(120,"age cannot be more than 120")])


     heartrate = models.IntegerField(default=60)
to 
    heartrate = models.IntegerField(default=60,validators=[MinValueValidator(1),MaxValueValidator(300,"heartrate cannot be more than 300")])


C:\Users\Student\Desktop\Untitled 
Folder\Python\ThirdProject>python 
manage.py makemigrations FirstApp 
Migrations for 'FirstApp':
  FirstApp\migrations\0002_patient_heartrate_alter_patient_age.py   
    - Add field heartrate to patient
    - Alter field age on patient  
have a look at 0002_patient_heartrate_alter_patient_age.py


to see the actual sql code u can run 

  <0002 here is 0002....file .py>
C:\Users\Student\Desktop\Untitled Folder\Python\ThirdProject>python manage.py sqlmigrate FirstApp 0002 
BEGIN;
--
-- Add field heartrate to patient
--
CREATE TABLE "new__FirstApp_patient" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "heartrate" integer NOT NULL, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "age" integer NOT NULL);
INSERT INTO "new__FirstApp_patient" ("id", "first_name", "last_name", "age", "heartrate") SELECT "id", "first_name", "last_name", "age", 60 FROM "FirstApp_patient";
DROP TABLE "FirstApp_patient";
ALTER TABLE "new__FirstApp_patient" RENAME TO "FirstApp_patient";
--
-- Alter field age on patient
--
-- (no-op)
COMMIT;


here were are creating a new table copying data from previous table and
dropping old date and remnaming new table to old table name


now run migrate
C:\Users\Student\Desktop\Untitled Folder\Python\ThirdProject>python manage.py migrate
Operations to perform:
  Apply all migrations: FirstApp, admin, auth, contenttypes, sessions   
Running migrations:
  Applying FirstApp.0002_patient_heartrate_alter_patient_age... OK


  updating the tables
  ========
  start the shell 
(terminal lshould always be command promot
by default when u open terminal it opens powershell , towards right botton beside the name
there will be + symbol click on that and select command prompt )
python manage.py shell 


>>> from FirstApp.models import Patient
>>> carl = Patient.objects.get(pk=1)
>>> carl
<Patient: carl and smith his age = 30>
>>> carl.last_name
'smith'
>>> carl.last_name = 'django'
>>> carl
<Patient: carl and django his age = 30>
>>> carl.save()
>>> Patient.objects.all()
<QuerySet [<Patient: carl and django his age = 30>, <Patient: susan and smith his age = 40>, <Patient: adam and smith his age = 40>, <Patient: karl and marx his age = 40>]>


Deleting the data
==========
>>> carl = Patient.objects.get(pk=1)                                1)
>>> carl.delete()
(1, {'FirstApp.Patient': 1})            --- this mean that it deleted the patient with index 1   
>>> Patient.objects.all()
<QuerySet [<Patient: susan and smith his age = 40>, <Patient: adam and smith his age = 40>, <Patient: 
karl and marx his age = 40>]>  



Connecting templates and DB models
===============
urls.py in Project  add FirstApp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('FirstApp/',include("FirstApp.urls"))
]

create listPatients in views.py
create urls.py in FirstAPP and register list_Patients

create templates/FirstApp in FirstApp
create list.html there


python manage.py runserver 8080
hit http://127.0.0.1:8080/FirstApp/
u will see <QuerySet [<Patient: susan and smith his age = 40>, <Patient: adam and smith his age = 40>, <Patient: karl and marx his age = 40>]>


administration
==========

# important all steps are here for creating a app
=================================
FourthProject
open cmd ad admin
cd C:\Users\Student\Desktop\Untitled Folder\Python\ 

python -m django startproject FourthProject 
cd FourthProject
python manage.py startapp FirstApp

lets start form the teamplates, views to models some people start from models and gooto views, and templates

under project level create templates/base.html for inherticance later, once this is done it needs to registered in DIRS in settings.py
        'DIRS': [os.path.join(BASE_DIR,'templates')],

under FirstApp , create templates/FirstApp 
with 3 htmls

add.html
delete.html
list.html

create views.py for those 3 htmls
def list(request), add, delete

create urls.py and connect the urlpatterns
also add usrl to urls.py in Project.


adding the app to installed apps see apps.py
    'FirstApp.apps.FirstappConfig',



in base.html lets add navigation bar using bootstrap
https://getbootstrap.com/ search for jsdeliver
u have the link <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">

get the javascript link as well<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>

add to head as 
 <!--css only-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <!-- javascript bundle with popper-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>

https://getbootstrap.com/docs/5.3/components/navbar/
here u have navbar
copied the codefrom 
https://getbootstrap.com/docs/5.3/components/navbar/#nav
copied the code from above and modified it to have url for list add and delete using the urlname and app name in urls.py

now lets add base.html using inheritance to list, add and delete

goto terminal change to command prompt
python manage.py runserver 8080

http://127.0.0.1:8080/FirstApp/list/

now lets work on the models
once the Car class is created lets run migrations

python manage.py makemigrations FirstApp      
Migrations for 'FirstApp':
  FirstApp\migrations\0001_initial.py
    - Create model Car

python manage.py migrate                      
Operations to perform:
  Apply all migrations: FirstApp, admin, auth, contenttypes, sessions   
Running migrations:
  Applying FirstApp.0001_initial... 
OK
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK



Now lets modify the templates and views
from views.py send a context with list of cars to list.html
<!--as we are using bootstrap lets use div class = container-->


now lets do add.html
create the form inside add.html and start server and hit submit
CSRF verification failed. Request aborted.

You are seeing this message because this site requires a CSRF cookie when submitting forms. This cookie is required for security reasons, to ensure that your browser is not being hijacked by third parties.

If you have configured your browser to disable cookies, please re-enable them, at least for this site, or for “same-origin” requests.

In general, this can occur when there is a genuine Cross Site Request Forgery, or when Django’s CSRF mechanism has not been used correctly. For POST forms, you need to ensure:

Your browser is accepting cookies.
The view function passes a request to the template’s render method.
In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL.
If you are not using CsrfViewMiddleware, then you must use csrf_protect on any views that use the csrf_token template tag, as well as those that accept the POST data.
The form has a valid CSRF token. After logging in in another browser tab or hitting the back button after a login, you may need to reload the page with the form, because the token is rotated after a login.
You’re seeing the help section of this page because you have DEBUG = True in your Django settings file. Change that to False, and only the initial error message will be displayed.

You can customize this page using the CSRF_FAILURE_VIEW setting.




It says we have to add  {% csrf_token %}
in views.py -- add
        # when the add page is opened for the first time it
        # comes to this else
        # and when submit is clicked we are not going anywhere as
        # form action is empty 
        # so it hits the same url again but with post
        return render(request,'FirstApp/add.html')
    
lets now do delete.html

Django administration
======================
start the sevrer and goto http://127.0.0.1:8080/admin
create the superuser frmo the command line
stop the server
python manage.py createsuperuser
username : saikrishna
mail: saikrishna1930@gmail.com
pwd: Django@098

we have authenticaiton and authorization screen
we will sese about authentication later
now lets see about admin access to the models we created

in admin.py 

from FirstApp.models import Car
# or from .models import Car
# Register your models here.

admin.site.register(Car)

now refresh the admin page u will see Cars Table with the data there
from there u can delete, add and edit the records
u can also see the history there


FifthProject
========================
Django forms
python -m django startproject FifthProject
cd FifthProject
python manage.py startapp FirstApp


let start with the templates and views
in FirstApp create templates/FirstApp
create rental_review.html and thank_you.html
views.py --- def the function with return render(request,'FirstApp/rental_review.html')

just create the skeleton like and empty htmla nd views with just return statement


and link in urls.py and also in projects/urls.py

add to FirstApp to installed apps in settings.py
    'FirstApp.apps.FirstappConfig',


now add some html to rental_review and tahnkyou.htmls to see everything is working
open terminal change to command prompt from powershell
start the server and hit

now lets work on rental_review.html
https://docs.djangoproject.com/en/4.0/topics/forms/

u only need to put the form tag and the submit button 
and the forms.py takes care of the form 


<!-- https://docs.djangoproject.com/en/4.0/topics/forms/-->
        <!-- https://docs.djangoproject.com/en/4.0/topics/forms/#rendering-fields-manually -->
        <!--https://docs.djangoproject.com/en/4.0/ref/forms/fields/-->
       

after filling rental_review.html lets fill views.py
run the server
at this moment we are not injecting the data in to DB we are just printing it
we can directly do that using ModelForms.


Django forms widgets and styling
==================
create app/static/app/custom.css
load static directory in html
link static css file connection
run migrate to load new app in settings.py (this is needed for new app
here i havw not channeged anything in settings.py so not needed)

rename rental_review.html to rental_review_old.html
and rental_review.html for loading static css file

create static/FirstApp in FirstApp
create custom.css
now link this static file using
in rental_Review.html
{% load static %} at top

in head 
    <link rel="stylesheet" href="{% static 'FirstApp/custom.css%}"?
and for div tag add myform which is defined in custom.css
run server and hit
http://127.0.0.1:8080/FirstApp/rental_review/


next is adding widgets 
if u see 
https://docs.djangoproject.com/en/4.1/ref/forms/fields/
all the form fields have widget 
goto to widgets 
https://docs.djangoproject.com/en/4.1/ref/forms/widgets/
lets goto forms.py and in in review field
review =forms.CharField(label="Please write your review here",
                                widget=forms.Textarea())

How to add styling to specific field this can be done in forms.py 
using the widget and attributes

 review =forms.CharField(label="Please write your review here",
                                widget=forms.Textarea(attrs={'class':'myform'}))
                                #attrs is a dictionary myform style  will be applied run time from custom.css
for each widget u can also look at attributes online on what attributes it is having
review =forms.CharField(label="Please write your review here",
                                widget=forms.Textarea(attrs={'class':'myform','rows':'6','cols':'8'}))
                                #attrs is a dictionary myform style  will be applied run time from custom.css
                                # we can add more attributes like rows and cols
                                # like below
                                #<textarea id="w3review" name="w3review" rows="4" cols="50">
                                # u can goto w3schools or any and look for the tag and add them to the dictionary
                                #https://www.w3schools.com/tags/tag_textarea.asp



Django Model Forms:
===================
ModelForm class automatically creates a form with fields connected to each model field.
#https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#field-types
most of the fields have one to one mapping to form fields 
but ther is no mapping for autofield and bigautofield as the user should be using the fields to modify the
primary keys in the DB 



lets create a new app
and regisrter in settings and urls
and copy files from FirstApp to secondApp
view,templates, static

1) create the class Review model in model.py
2) register this model in administration in admin.py 
from .models import Review
admin.site.register(Review)
3) now run makemigrations and migrate
python manage.py makemigrations 
python manage.py migrate

create superuser
python manage.py createsuperuser
Username (leave blank to use 'student'): saikrishna
Email address: saikrishna1930@gmail.com
Password: Django@098

now start the server  and test the model from the admin page
http://127.0.0.1:8080/admin
Click on reviews and add a review and save

in forms.py remove everything and 
from .models import Review
from django.forms import ModelForm

and create ReviewForm class
now start the server and hit http://127.0.0.1:8080/SecondApp/rental_review/

goto views.py and save the form data in the if block
            form.save()

ModelsFormsCustomization is also done in models.py 
using  labels
will add validators to models.py
  # these validators are automatically  checked in views.py in if form.is_valid
    # as all these validators are added make migration and run migrations

  # these validators are automatically  checked in views.py in if form.is_valid
    # as all these validators are added make migration and run migrations
    # now if u click submit by filling rating as 9
    # it doesnt do anything becoz the data is not valid but it is not reporting any error
    # to report the error usse {{field.errors}} in the rental_review.html
    # now if u fill  7 it automaticalkly shows the error message as Ensure this value is less than or equal to 5.
    # if u fill 0 it shows  Ensure this value is greater than or equal to 1.

    # 
above are the default error messages u can also add ur own custom error messages in forms.py
but u need to identify the keys inthe dictionary 

https://docs.djangoproject.com/en/4.1/ref/forms/fields/#built-in-field-classes
each field is like class BooleanField(**kwargs)¶
Default widget: CheckboxInput
Empty value: False
Normalizes to: A Python True or False value.
Validates that the value is True (e.g. the check box is checked) if the field has required=True.
Error message keys: required

search in the page for integerfield it shows
Error message keys: required, invalid, max_value, min_value, step_size

so now lets add to  forms.py

error_messages = {
            'stars':{
             'min_value': 'min value should be 1',
             'max_value':'max value should be 5'

            }
        }



Class Based views
==========
class based views automatically generate web pages with forms from a model class

SixthProject
FirstApp - connecting template to a View
create templates/FirstApp
home.html with just welcome text

we know function based views in views.py we define a function and connect it to a template
with return statement 
and add to urls.py 
in urls.py path() expects a view function here it is  home_view
add to installed apps
create models.py Teacher class
and run migrations
verify its working by running the server

Template View:
=============
in views.py 
add a new view ThankYouView for class based views -- template view

from django.views.generic import TemplateView

add thankyou.html
add to urls.py
Form View
============
in views.py create a class ContactFormView

in the FirstApp create a file forms.py and create ContactForm class
create contact.html
in urls.py link

https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-editing/


If we are using success_url we have to use reverse_lazy().
If we are reversing inside a function we can use reverse().


Model based class based views:
===========================
create, detail, update, delete, list

it automatically looks for :model_form.html (all smalls)
in views.py add TeacherCreateView
in models.py we have created Teacher class earlier
so it automatically looks for teacher_form.html

in templates create teacher_form.html

the moment we hit the submit button it automatically saves .save() after all the fields are validated
add to urls.py and home.html



ListView:
===============
create class TeacherListView
it automatically looks for :model_list.html (all smalls)
create teacher_list.html
add to urls.py and home.html


DetailView
==============
create class TeacherDetailView
it automatically looks for :model_detail.html (all smalls)
add to urls.py 
    path('teacher_detail/<int:pk>',views.TeacherDetailView.as_view(),name='detail_teacher'),
we are passing the pk in the url
add a link to teacher_list.html for detail view

UpdateView
============
create class TeacherUpdateView
    # it share model_form.html that create view uses
urls.py
add a link to teacher_list.html  for update view

Delete View
====
    # it looks for model_confirm _delete.html
in views add TeacherDeleteView
add to urls.py
create teacher_confirm _delete.html
add to teacher_list.html


U can use function based views when u want to write ur on function.
rather than class based views

 User Authentication 
 =========================
there is a folder User Authentication DownloadedFromResources  ---- this i downloaded form Resources

but i will create one more project
open cmd in admin mode
i used >python -m django startproject Seventh_AuthProject 
project is like library
cd Seventh_AuthProject
python manage.py startapp FirstApp
firstapp is like catalogue
register app in settings.py
run migrations -makemigrations and migrate
create urls.py in FirstApp
add FirstApp.urls to urls.py in FirstProject

in urls.py in Project
from django.views.generic import RedirectView
#     path('',RedirectView.as_view(url='FirstApp/')), www.example.com -->www.example.com/FirstApp
# to redirect http://127.0.0.1:8080/ to http://127.0.0.1:8080/FirstApp/


in views.py create index function with just one line return HttpResponse("Hello")
def index(request):
    return HttpResponse("Hello")
    # if u notice this it doesnt have any html page in the templates we are just returning the HttpResponse
'''
add to urls.py
run the server and hit http://127.0.0.1:8080/

models Seventh_AuthProject
=============
create some models in models.py for  genre, book, language, author, bookinstance(specific physical copy)

book has a foreign key for author 
an author can write multiple books so its better to have author as a separate table.


once all the models are saved run the server to see for any errors

if no errors run the migrations
python manage.py makemigrations
python manage.py migrate

register the models in admin.py
create a superuser
C:\Users\Student\Desktop\Untitled Folder\Python\Seventh_AuthProjectpython manage.py createsuperuser 
Username (leave blank to use 'student'): saikrishna
Email address: saikrishna1930@gmail.com
Password: Django@098
Password (again): Django@098
Superuser created successfully.

create example instances
run the server and goto http://127.0.0.1:8080/admin


First add language - english
add 3 genres - mystery , comedy , entertainer
add author -sai krishna 
add book -  in author dropdown u automatically get the author name
    class Meta:
        # this is to dictate  the behaviour in the admin view
        ordering = ['last_name','first_name']
        # while  doing add book in the admin view the dropdown for author showed the names of author 
        # as lastname, firstname
for genre in book u can hold ctrl and select more than one genre

now lets add book instance
id field is automatically filled there as it is a UUIDField AND 


Pages setups
==========
lets create the views here for the models.
in views.py
modify the views.py --index function to return some statistics and add
FirstApp/templates -- index.html

in views.py add a generic CreateView for the book
in templates add model_form.html -- Book_form.html
and add in urls.py
run the server and test 
http://127.0.0.1:8080/FirstApp/create_book

on submitting u get the error :
Reverse for 'book_detail' not found. 'book_detail' is not a valid view function or pattern name.
becoz by  it is trying to goto  reverse("book_detail" but it is not yet defined

# on creation of a book it goes to this url automatic.
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})


CreateView inherits from BaseCreateView
BaseCreateView in herits  ModelFormMixin

somewhere if form is valid it is calling get_success_url
    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        if self.success_url:
            url = self.success_url.format(**self.object.__dict__)
        else:
            try:
                url = self.object.get_absolute_url()


as in our case we have not defined success url it is calling our get_absolute_url
but in out get_absolute_url we have used  return reverse("book_detail", 
but book_detail is also not defined to it is throwing error.




lets define the book_detail view.
in views.py create class BookDetail(DetailView)  and in templates create book_detail.html
and add book_detail as name  to urls.py
run the server and test 
its working now

User Authentication with Django User model
=====================================

lets add users.


dJANGO HAS default authentication with django.contrib.auth in installed apps
in middleware we see session middleware and authentication middle ware.


from the django admin page -- 
click on add .0010_alter_group_name_max_length
name: Library members
in the Available permissions
filter u will see each model and different permission like add, delete, change, view
for now dont select any persmissons and save the group.

in users:
add user
for now we are giving username and pwd
later it will be real user.
username : myuser
pwd: Django@098

save the user
goto users , select the user -- > 
u will have options to select groups for this user,
also options to select user permission  for this user.

For now add the LibraryMembers grps to this user(myuser) and save


lets add to urls.py in project level 
path('accounts/',include('django.contrib.auth.urls'))

by adding above we iwll have
This will include the following URL patterns:
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']


https://docs.djangoproject.com/en/4.1/topics/auth/default/



'''
http://127.0.0.1:8080/accounts/login/

TemplateDoesNotExist at /accounts/login/
registration/login.html
'''

by adding that line those urls are avaiable to us but not the templates
we have to create the templates



create templates/registation folder at the project level:
where manage.py is there

in settings.py 
import os and add to DIRS
        'DIRS': [os.path.join(BASE_DIR,'templates')],


create login.html in the registration:
<!-- 1. check for form.errors
2. user is logged in but no access
3. user not logged in 
4. form login -->

after creating login.html hit
http://127.0.0.1:8080/accounts/login/
then 
First time form.errors will not be present so that if will fail
if next --that if also fails as Django didnt send anything back yet
so only the form is displayed.

now if u enter wrong username/password:
form.errors will be true

now if u enter myuser/Django@098 or the admin --- saikrishna/Django@098
it takes u to 
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8080/accounts/profile/
becoz it takes u to login redirect and u can actually setup login redirect yourself.

if we dont want to create this 
we can add LOGIN_REDIRECT_URL = '/' IN the settings.py this takes to the home page.

here it is taking to http://127.0.0.1:8080/FirstApp/ as per the urls.py in project level.

Now the views should decide whether someone is loggedin or not to see the page.
==========================
User authentication on views:
=================
2 ways : 
1. decorators for function based views
2. mixins for class based views

in index.html add the if user.is_authenticated block
now  hard refresh -- http://127.0.0.1:8080/FirstApp/ 

HOMEPAGE
Total Books: 4

Num Available: 0

You are not logged in

LOGIN HERE

if u click on login here and login 
then u see

HOMEPAGE
Total Books: 4

Num Available: 0

You are Logged In

Welcome: myuser

LOGOUT HERE

lets create logged_out.html in templates


1. decorators for function based views
================
in views.py create a function my_view
create my_view.html in templates/FirstApp
my_View.html is displayed only for logged in users.
add to urls.py


<!-- # if u hit http://127.0.0.1:8080/FirstApp/my_view it redirects to
# # http://127.0.0.1:8080/accounts/login/?next=/FirstApp/my_view/ 
with next parameter in the url-->
{% if next %} <!-- if user is logged in but no access  or not logged in then Django sends a string query called next  which means goto next page-->

   

2. mixins for class based views
==================
http://127.0.0.1:8080/FirstApp/create_book/
at this moment BookCreate class in views.py doesnt have any authentication verification
lets make something like user should be logged in and users grp is equal to librarian then they should access create_book.
import LoginRequiredMixin and the BookCreate class should inherit LoginRequiredMixin
in views.py class BookCreate(LoginRequiredMixin,CreateView): #book_form.html

logout in http://127.0.0.1:8080/FirstApp/ and 
now hit http://127.0.0.1:8080/FirstApp/create_book/
it redirects to http://127.0.0.1:8080/accounts/login/?next=/FirstApp/create_book/




User registration and forms:
=======================
if u want you could use the build in user object to create users manually using your own form.
Luckily for us, Django provides quite a few built in forms and views based off the user class that's
built in the Django.
Let's explore some of these in the documentation and in our code.

https://docs.djangoproject.com/en/4.1/topics/auth/default/#using-the-django-authentication-system


I should point out that there's full API documentation.
https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User
So if you want, you could continue to customize user objects by actually inheriting the user class
and then adding more fields to it.
If you needed something like let's say a profile picture for your particular website, you could start
linking that inside the user object.
Or probably more appropriately, could we do something like a profile picture model that we link through
a foreign key to a user, lots of different ways to actually tackle that sort of problem.
Then as I mentioned, you can create users directly.
So the way you could do this is you could say from Django that can trim the off but models import user
and just with this one line especially it means that you have full access to the user class.

you can create users directly.
So the way you could do this is you could say from Django that can trim the off but models import user
and just with this one line especially it means that you have full access to the user class.
So everything we learned about creating forms or creating instances inside a model class for adding
a new row to a database that can all be done for the user as well.
You can see it's just user.
The objects that create user and all that knowledge that you know already can be done automatically
for you using the user class.
So this allows you to do a lot of things the way you already know how.
You're just swapping out your typical model for a user model.


https://docs.djangoproject.com/en/4.1/topics/auth/default/#permissions-and-authorization ***

https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.views ***

https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms

If I wanted to create a new user, I could manually create a little function based model form setup
thing that says, okay, user, the object that create new user, etc. and do it all manually.
But the user creation form can save a lot of time if we don't want to do it all manually.
lets see how to use https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm for creating a user.

in views.py import from django.contrib.auth.forms import UserCreationForm 
and create class SignUpView
add SignUpView to urls.py
and create the signup.html

lets test the code:
run the server and hit http://127.0.0.1:8080/FirstApp/signup/
it redirects to login page.
the user gets added to users, we can verify that from admin page. http://127.0.0.1:8080/admin/auth/user/?o=5.1


you coudl also do it like https://docs.djangoproject.com/en/4.1/topics/auth/default/#creating-users
by grabbing  the information from a custom form I created and then create that user.
Obviously this is such a common request that the user creation form object has already been created
for you by Django.
But I just want to point that out that you technically, just by viewing this box of code here(https://docs.djangoproject.com/en/4.1/topics/auth/default/#creating-users)
, you
already know how to use all the skills to create a user.
It's just you have to remember that all you have to do is import user and then you can do that itself.



User specific pages
===================
lets associate a book instance to a specific User
in the BookInstance class add user(borrower)as foreign key,


    book = models.ForeignKey("Book",on_delete=models.RESTRICT,null=True) # whether it is "Book" or
     # Book without quotes it is not making any difference. i tried creating a book instance in both cases it worked fine.
  borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    ''' but here use User withour quotes,  if u use "User" we are getting errors FirstApp.BookInstance.borrower: (fields.E300) Field defines a relation with model 'models.User', which is either not installed, or is abstract.
FirstApp.BookInstance.borrower: (fields.E307) The field FirstApp.BookInstance.borrower was declared with a lazy reference to 'models.user', but app 'models' isn't installed.


the reason might be User is from a different package'''


make migrations and migrate

>python manage.py runserver 8080  
hit http://127.0.0.1:8080/admin/
login as superuser saikrishna/Django@098

goto book instances 
and add a borrower -- myuser for a book

setup  a page and see the books borrowed by a user.

There's lots different ways we could do this, but it probably makes sense to use a generic list view
where I just run a query of book instances and actually filter them based off the user.
So there's different ways you could do this.
You could do a query based off the user and grab their books.
But I think it actually makes more sense to take advantage of the list view.
That way you can actually do it from a book instance perspective.
So that will actually make our life a little simpler as far as defining the view.


create class CheckedOutBooksByUserView in views.py
in urls.py add it
create profile.html in templates

start the server
 http://127.0.0.1:8080/FirstApp/ -- logout 
and login as myuser
and goto http://127.0.0.1:8080/FirstApp/profile
it will show the books checked out by myuser2




Deployment
================
https://linode.com/lp/try/?ifso=perian
mail : saikrishna1930@gmail.com
username : saikrishna1930
7867848372
https://cloud.linode.com/linodes

goto marketplace and select Django
scroll down there will be Django options:
they are like superuser options

username : saikrishna1930
pwd: Django@098
mail id : saikrishna1930@gmail.com
images: let ie be Debian 10
region : goto speedtest page to find out the closest region based on the target audience
region : Dallas Texas 
linode plan : shared CPU is enough for our website
chose Linode 2GB 
leave the linode label and tags u can leave it
root password: Django@098

u can leave everything and click on create linode

Summary
1 CPU Core
50 GB Storage
IP Addresses
139.144.37.242 -- default port is 8000

2 GB RAM
0 Volumes
IP Addresses
2600:3c00::f03c:93ff:fefc:102a



summary shows  139.144.37.242 as IP address. The default port is 8000.
this means if u  hit 139.144.37.242:8000, the remote computer runs DJango.



SSH Access
ssh root@139.144.37.242

LISH Console via SSH
ssh -t saikrishna1930@lish-dallas.linode.com django-us-central



mac/linux users can directly enter ssh root@139.144.37.242
 at terminal


windows users can use powershell to connect  but you actually have to first install the Open SSH client,
which is done through manage optional features on windows.

windows - so here I am inside a visual studio code open the folder - C:\Users\Student\Desktop\Untitled Folder\Python\Seventh_AuthProject
Remember, we can hit Terminal to create a new terminal, and the default terminal should be PowerShell.
in powershell enter :
enter ssh root@139.144.37.242
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
enter password as Djando@098


Now really, the final step is to be able to store a copy of our code on GitHub either publicly or privately
and then update our servers Django Project Code with any code if updated on GitHub.


root@139-144-37-242:~# cd /var/www
root@139-144-37-242:/var/www# ls
DjangoApp
root@139-144-37-242:/var/www# cd DjangoApp/
root@139-144-37-242:/var/www/DjangoApp# 
ls
db.sqlite3  DjangoApp  manage.py
root@139-144-37-242:/var/www/DjangoApp#  ps aux
root      6406  0.0  1.7  45904 35396 ?        S    14:34   0:00 python3 manage.py runserver 0.0.0.0:8000
Django server is running continously as a background process


to install git : apt-get install git
goto github.com. create a repo.
repository : django-example-linode1

click on create u will see  a screen with below

…or create a new repository on the command line

echo "# django-example-linode1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sk1930/django-example-linode1.git
git push -u origin main

 we actually need to create what's known as a personal access token.
The personal access token will essentially allow us to have a password that will allow the little server
to push changes here to our example on GitHub to do that.
Go ahead and duplicate GitHub tab.
And then at the top right.
Go to Settings.
Scroll down until you see developer settings.
Then go to personal access tokens.
Then you are going to click Generate New Token.
You can go ahead and give yourself a note as far as what's this token for?
So I'll say this is for LinodeDjangoDeployment.
You can also make this exploration for this token so I can make this expire in seven days, for example
Under Select scopes
select repo checkbox and click Generate token
u will get a token like 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


right click acts as paste in powershell.

paste these commands in cmd line copy all the 7 lines and right click on command line
it automatically executes one line after the other and in the last 
command is not executed it is just pasted ---click enter
and it will ask for username and pwd
username is sk1930
pwd is that token 

echo "# django-example-linode1" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/sk1930/django-example-linode1.git
git push -u origin main

it will ask for username and pwd
username is sk1930
pwd is that token 

we have already opened VS code and connected to shell root@139-144-37-242:/var/www/DjangoApp# that
means we are adding the repository to our remote server.

git add . 
git commit . -m "my second commit"
git push -u origin main


now open github desktop foe easy access
under current repository click on add -- clone a repository and select sk1930\django-example-linode1 - 
select local path C:\Users\Student\Desktop\Untitled Folder\Python\Django
it will then show path as C:\Users\Student\Desktop\Untitled Folder\Python\DjangoApp\django-example-linode1
and choose clone


open C:\Users\Student\Desktop\Untitled Folder\Python\Django\django-example-linode1 in vs code
open terminal switch to command prompt and 
python manage.py startapp otherApp
goto views.py 
just create a simple_view function based view which doesnt need any template
like return HttpResponse("Hello")
create urls.py on otherApp 
also add otherApp to urls.py in project     path('otherApp', include("otherApp.urls").site.urls),

now we have to push these changes to github.
lets goto github desktop
commit changes to main and push




 now in the remote client we have to publicly
 open terminal do ssh and cd /var/www/DjangoApp
 do git pull

now hit 
IP Addresses
139.144.37.242 -- default port is 8000
http://139.144.37.242:8000/otherApp






in the end go here https://cloud.linode.com/account/settings and click on close account to avoid charges
