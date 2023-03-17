# CRM 

![My website](https://crm2-naq4z.ondigitalocean.app)


## Features:
- Full featured CRM system
- Extend Authentication system: Login, Logout, Reset-Password 
- Built-in signals dispatchers like – pre_save, post_save
- Uploading files options (Images and Documents)
- Only Class Based Views as well with the Forms
- Sending Email option ( inside the console)
- Filter results ( based on the user )
- Lead & Agent management under one organization:
    - Create,  View , Update and delete Lead / Agent
    - Assign Each lead to Category and Agent
- Secured app both in backend and frontend
- Advance and flexible dashboards with analyses
- Combining the “flash message” feature
- Designed web app displays for users
- Customized admin site Interface





## Getting started
1. Create your own virtual environment , and  don't forget to activate it | [toturial link](https://bit.ly/3YQlTDn)
2. Install all of the packages which is mentioned in ```requirements.txt``` file
3. Create a new file named ```.env``` inside the ```/core``` folder ( must be in the ```/core``` )
4. Copy all of the variables inside ```core/.template.env``` to your ```.env``` file and fill your own values to them 
5. Download **Postgresql** and configure the connection parameters with to your own db in ```settings.py```, [see link for tutorial for more explanation](http://shorturl.at/dxEZ6) 
6. Learn how to create your own ```SECRET_KEY``` : https://bit.ly/42atuj1 and copy it to ```.env``` file
7. Create a superuser for your app (it will be used as the first user) run in the terminal ```python manage.py createsuperuser ```
8. Run ```export READ_DOT_ENV_FILE=True``` inside your terminal so that your environment variables file will be read.
9. Run ```python manage.py makemigrations``` inside your terminal
10. Run ```python manage.py migrate``` inside your terminal
11.  After migrating, Run ```python manage.py runserver``` inside your terminal to run the server

If you have closely followed the instructions, you suppose the see the home html page and you can loging thesystem using the superuser credentials



## Description
In this project I have developed an advanced CRM app.
The system manages two users types: 
1. Organizers
2. Agents


<ins></ins>


Each type of user has a different level of permissions and those are enforced by using the <ins>Django authentication system.</ins> 
Under each Organizer there are several Agents. Under each Agent there are several leads:


![היררכיה CRM](https://user-images.githubusercontent.com/113801007/225297061-e1189684-8e99-4c40-a5ef-1ef2c469da8a.JPG)

<ins>Organisor</ins>
The “Organizer” user is created right after a new user has registered the app. From the moment the Organiser user is created, a new UserProfile instance is also created. UserProfile is a model representing an Organisation, it has only one field, a ForeginKey field pointing to the User model,  and it is attached to the Organiser User that has been created.

this is an example of three different organization using the same CRM system:
![3 irrachi](https://user-images.githubusercontent.com/113801007/225299472-67e21789-7a1d-4243-8e24-1fa032d622b9.JPG)

Any Agent and Lead has the “organization” field (pointing to the UserProfile model). And that separates Agents and Lead between the organizations in the system. 

Each Organizer User has the permission to view and edit only leads and agents belonging to his organization. The same with agents: they have permissions to view Leads only from their organization that is attached to them.

As mentioned before, those permissions are enforced by using the **Django Authentication system.**


<ins>Agent:</ins>
As was mentioned before, the Agent user has only the permission to view the leads attached to his organization . Agents can be edited (created, updated and deleted) only by an Organizer. Form the moment an agent is created, his email address is stored in the db and the agent can login the system only after completing the Resetting Password Via the “forgot password page”

<ins>Lead:</ins>

To make it clear: leads do not take part as a user in my app. They are only tracked by Agents and Organizer users. Leads can be classified to three kinds of fields:
1. Organisation
2. Agent
3. Category
As was mentioned previously, only an organizer can edit lead’s field.

<ins>A few words about combining the Django auth systme</ins>

Django authentication provides both authentication and authorization together and is generally referred to as the authentication system, as these features are somewhat coupled.

The authentication system of Django is mainly based on the User model, which I have customized a bit : adding the <ins>is_organisor</ins> and <ins>is_agent</ins> fields.

![image2](https://user-images.githubusercontent.com/113801007/225300646-18b8887e-48ce-4bf7-b639-73bde71781f2.png)

<ins>Login, Logout, Register, ResetPassword</ins>
Moreover, Thanks to the  following Django classes:
- LoginView
- SignUpView
- LogoutView
- PasswordResetView
- PasswordResetDoneView
- PasswordResetConfirmView
- PasswordResetCompleteView

I created the Login, Logout , Register and Reset Password functionalities.
Those CBV( class based view ) gave me the tools to track each user who has sign to the app and send back HttpResponse objects <ins>based on their permissions.</ins> 


<ins>Maintaining the security principles</ins>

<ins>Secure the Backend</ins>

my views were secure thanks to two django-built-in classes:
* OrganizorAndLoginRequiredMixin
* LoginRequiredMixin
Each view inherit from one of those classes and thanks to that, user without permissions to a specific view will be redirect to the Login page or the leads list page.

![image1](https://user-images.githubusercontent.com/113801007/225301742-3bc7db1e-0723-4d3e-9f61-d9f86011a844.png)

<ins>Secure the Frontend</ins>
In each HTML template I used the Django template (known as Jinja Engine) to Determine whether the user who sent the request has permission to access different links connecting to different views in my app.


<ins>using only Class Based View</ins>
At the beginning it was a real challenge to learn how to use CBV with django. But after a while I got used to it and then learned the power behind using Abstract classes to handle different kinds of requests. The usage of forms in my app, the django authentication system, and each view are all based on classes and I am very proud of it.

<ins>The DataBase - PostgreSQL</ins>
I learn how to connect my Django app to Postgresql - a much more scalable DB with much more benefits compare to the SQLITE:
- It has the ability to handle simultaneous access by multiple users. 
- Has the ability to store nearly any type of data that you may need to store in your database.- 
- Comes with many security features, which makes PostgreSQL a secure DBMS for the storage of sensitive and private data.

With those benefits come the Disadvantages: it is a complex DB and it might take much longer to configure it.

There is one positive thing about changing your DB in the Django project: once you configure the right db connection parameters, you can use Django the same as before, because the complex process of converting django syntax into sql queries is made behind the scene by Django engine that know how to create sql queries for different kinds of db. Thanks to that you can always change your DB with few customizations.

###### Distinctiveness and Complexity

<ins>The distinction of my app comes in several aspects:</ins>
 
1. Unlike the course, in my project I have used only class based views and not function base views
2. Relational tables: some of my model’s fields have OneToOne relationship, some of them ManyToMany relationship and some of them OneToMany. To retrieve instances from different models I had to use those relationships to query instances from other tables.
3. Ui interface is much more complex and well design:
- Business styled flat dashboard including  forms, tables, charts, and modals.
- Light/Dark Sidebar Styles
- Well styled landing page
- Used the django crispy forms package to make each form in my website look better
4. My project put a lot of attention on the security aspects, both in the frontend and backend sides. **(I have already explained a lot about the django authentication system and how I used it.)**
5. My project involves new features: sending emails, signal dispatchers, FormValidation, Flash messages, Custom Domain Interface and many other things ( things new which we haven't learned in the course)


## The projects files and folders:

![project folder](https://user-images.githubusercontent.com/113801007/225306487-485df735-d105-4fee-a04f-bdf8f7c644d8.JPG)

<ins></ins>

1. <ins>core/</ins>
where all of my projects file settings are located, including the .env file. In <ins>core/urls.py</ins> the main url paths are configured and other advanced url path configure in <ins>agents/urls.py</ins> and <ins>leads/urls.py</ins> 

2. <ins>templates/:</ins>
All of my templates are located in <ins>/template</ins>  and all of the login,register,reset-password are located in <ins>/template/registration/</ins>

3. <ins>static/:</ins>
my static files are located in <ins>/static</ins> but in production they are located in <ins>/static_root. the connection of all html files to a all of the static files is done thanks to the {% load static engine at the begining %}
</ins>

4. <ins>leads/:</ins>
a big portion of my project’s scripts are located in that folder.
all of my <ins>models</ins> are located there, all of the views are written there (except the agent view). In <ins>leads/forms.py</ins> there are a bunch of forms classes that were written.

5. <ins>agent/</ins>
all the agent views are located in <ins>agents/view.py</ins> as well with the form <ins>agents/forms.py.</ins> 


















 
