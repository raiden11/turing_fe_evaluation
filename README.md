# turing_fe_evaluation


# Initialize the backend django project
RUN `django-admin startproject backend`
RUN `python manage.py startapp mytms`
Added mytms in INSTALLED_APPS in backend/settings.py
RUN `python manage.py startapp makemigrations`
RUN `python manage.py startapp makemigrations`
Created models.py in mytms/models.py having the following models: Campaign, Member, Task
Created serializers.py in mytms/serializers.py having the following serializers: CampaignSerializer, MemberSerializer, TaskSerializer
Created superuser with username: turing, password: turing using command: `python manage.py createsuperuser`
Created admin.py in mytms/admin.py having the following admin classes: CampaignAdmin, MemberAdmin, TaskAdmin
Created a management command to create campaigns, members, tasks in mytms/management/commands/createdummydata.py
RUN `python manage.py createdummydata`

- Admin panel can be accessed at: http://localhost:8000/myadmin/

# Initialize the frontend (Used create-react-app with typescript template)
RUN `npx create-react-app frontend --template typescript`
Created personal info component with 3 fields
Created professional info component with 3 fields


