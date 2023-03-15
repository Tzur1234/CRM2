# CRM 

## Description
In this have developed an advanced CRM app.
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

<ins>Backend</ins>

my views were secure thanks to two django-built-in classes:
* OrganizorAndLoginRequiredMixin
* LoginRequiredMixin
Each view inherit from one of those classes and thanks to that, user without permissions to a specific view will be redirect to the Login page or the leads list page.







 
