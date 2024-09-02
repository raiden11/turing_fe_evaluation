# turing_fe_evaluation


# Initialize the backend django project
RUN `django-admin startproject backend` <br/>
RUN `python manage.py startapp mytms`<br/>
Added mytms in INSTALLED_APPS in backend/settings.py<br/>
RUN `python manage.py startapp makemigrations`<br/>
RUN `python manage.py startapp makemigrations`<br/>
Created models.py in mytms/models.py having the following models: Campaign, Member, Task<br/>
Created serializers.py in mytms/serializers.py having the following serializers: CampaignSerializer, MemberSerializer, TaskSerializer<br/>
Created superuser with username: turing, password: turing using command: `python manage.py createsuperuser`<br/>
Created admin.py in mytms/admin.py having the following admin classes: CampaignAdmin, MemberAdmin, TaskAdmin<br/>
Created a management command to create campaigns, members, tasks in mytms/management/commands/createdummydata.py<br/>
RUN `python manage.py createdummydata`<br/>
- Admin panel can be accessed at: http://localhost:8000/myadmin/<br/>
TODO:
Creating viewsets

# Initialize the frontend (Used create-react-app with typescript template)
RUN `npx create-react-app frontend --template typescript`<br/>
Created personal info component with 3 fields<br/>
Created professional info component with 3 fields<br/>

TODO: 
Create navigation between personal info and professional info pages <br/>
Use RTK Query to make API calls to the django backend<br/>
Implement timeout 30 minutes <br/>


