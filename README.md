# turing_fe_evaluation


# Initialize the backend django project

### App development steps
```sh
django-admin startproject backend
```
```sh
python manage.py startapp mytms
```
```sh
python manage.py startapp makemigrations
```
```sh
python manage.py startapp migrate
```
```sh
python manage.py createdummydata
```
```sh
python manage.py createsuperuser
```

- Created models.py in mytms/models.py having the following models: Campaign, Member, Task<br/>
- Created serializers.py in mytms/serializers.py having the following serializers: CampaignSerializer, MemberSerializer, TaskSerializer<br/>
- Created admin.py in mytms/admin.py having the following admin classes: CampaignAdmin, MemberAdmin, TaskAdmin<br/>
- Created a management command to create campaigns, members, tasks in mytms/management/commands/createdummydata.py<br/><br/>

### Todos
Creating viewsets

### To run the app
```sh
python manage.py runserver
```
Admin panel can be accessed at: http://localhost:8000/myadmin/<br/>



# Initialize the frontend (Used create-react-app with typescript template)

### App development steps
```sh
  npx create-react-app frontend --template typescript`
```
Created personal info component with 3 fields<br/>
Created professional info component with 3 fields<br/>

### Todos
Create navigation between personal info and professional info pages <br/>
Use RTK Query to make API calls to the django backend<br/>
Implement timeout 30 minutes <br/>

### To run the app
```sh
  npm install && npm start
```
App can be accessed at: http://localhost:3000/

