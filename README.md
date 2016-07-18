# Django React Bootstrap

## Setup
```
git clone git://github.com/gryevns/django-react-bootstrap.git
virtualenv .venv
source .venv/bin/activate
pip install -u requirements.txt

cd bootstrap
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## URLs
URL                       | Detail
------------------------- | ---------------------
127.0.0.1:8000/           | ReactJS index
127.0.0.1:8000/admin/     | Django admin
127.0.0.1:8000/api/users/ | Django Rest Framework
