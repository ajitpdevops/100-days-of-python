Resource - https://www.youtube.com/watch?v=Vv-zJJG0hj8

pip -m venv venv [Create a virtual environment]
pip install django [Install Django]
django-admin
djnago-admin --version
django-admin startproject tealcrm .
django-admin startapp employee || python manage.py startapp employee
python manage.py runserver 8080
python manage.py makemigrations employee
python manage.py migrate

### Django Tips - 
- APP_DIR: True in settings.py means template folders in apps will be automatically looked for the templates
- Create a folder with app name inside your template folders. This is a best practice

### DTL - 
- Difference between extend and include (include is suitable for navbar where extend is more suitable for base templates)
- Load static files - {% load static %}
- When calling dictionary instead of {{ myDictionary['some_key'] }} you use {{ myDictionary.some_key }}
- When calling functions instead of {{ result_from_a_function() }} you use {{ result_from_a_function }}

