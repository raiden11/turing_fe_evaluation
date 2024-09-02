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
RUN `python manage.py startapp makemigrations`<br/>
```
```sh
RUN `python manage.py startapp migrate`<br/><br/>
```
Created models.py in mytms/models.py having the following models: Campaign, Member, Task<br/>
Created serializers.py in mytms/serializers.py having the following serializers: CampaignSerializer, MemberSerializer, TaskSerializer<br/>
Created superuser with username: turing, password: turing using command: `python manage.py createsuperuser`<br/>
Created admin.py in mytms/admin.py having the following admin classes: CampaignAdmin, MemberAdmin, TaskAdmin<br/>
Created a management command to create campaigns, members, tasks in mytms/management/commands/createdummydata.py<br/><br/>
RUN `python manage.py createdummydata`<br/>
- Admin panel can be accessed at: http://localhost:8000/myadmin/<br/>

### Todos
Creating viewsets

### To run the app
```sh
python manage.py runserver
```



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


