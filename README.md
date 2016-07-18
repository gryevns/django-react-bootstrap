# Django React Bootstrap

Lightweight boilerplate for a Django backend and ReactJS frontend. Uses Django Rest Framework to create RESTful APIs which can be consumed by React. Webpack used to watch for JS changes and rebuild bundle served via Django template.

## Setup
```
git clone git://github.com/gryevns/django-react-bootstrap.git
cd django-react-bootstrap
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
npm install

python manage.py migrate
python manage.py createsuperuser
nohup python manage.py runserver &
npm start
```

## JWT Authentication
```
curl -X POST -d "username=<username>&password=<password>" http://localhost:8000/api-token-auth/
curl -H "Authorization: JWT <token>" http://localhost:8000/api/users/
```

## URLs
URL                       | Detail
------------------------- | ---------------------
127.0.0.1:8000/           | ReactJS index
127.0.0.1:8000/admin/     | Django admin
127.0.0.1:8000/api/users/ | Django Rest Framework
