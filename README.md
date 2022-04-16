# Innowise-Task

# Технологии
- Python 3.8
- Django + Django Rest Framework
- PostgreSQL 
- Docker + Docker-compose
- Celery + Redis

# Стилизация кода
- flake8
- isort

Бд для тестирования:
```$xslt
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'my_db',
'USER': 'root',
'PASSWORD': 'root',
'HOST': 'pg_db',
'PORT': '5432',
```

- Для работы с проектом необходим установленный докер:
```$xslt
docker-compose up --build
docker-compose run backend python manage.py makemigrations
docker-compose run backend python manage.py migrate
```

- Запуск тестов:
```$xslt
docker-compose run backend python manage.py test rest.tests
```

- Суперпользователь:
```$xslt
docker-compose run backend python manage.py createsuperuser
```

- Сервер доступен по адресу [127.0.0.1:8000](http://127.0.0.1:8000/)


