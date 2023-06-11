# Test for UTF

----

## Стек

- Python 3.8
- Django 3.2
- DRF 3.12
- Debug Toolbar
- Pytest
- Docker

----

## Что было сделано:

1. Constraint'ы на FoodRelationship
2. Запрос через Django ORM
3. Запрос через Django Raw
4. Тесты на Pytest
5. Docker - образ
6. Абстракции на поля моделей.
7. Абстракция на модели.

P.S. Запрос через ORM создаёт 3 запроса. Через Raw создаёт ещё больше, но если посмотреть корневой запрос через toolbar, то он выдаёт то, что надо)

----

## Немного про переменные окружения (.env)

 - SECRET_KEY - secret_key в settings.py
 - DEBUG_VALUE - если TRUE то подключается debug_toolbar.
 - RAW_QUERY_VALUE - если TRUE то работает ViewSet на Django Raw. (в остальных случаях работает Django ORM)

P.S. В репозитории DEBUG_VALUE = TRUE , RAW_QUERY_VALUE = FALSE

----

## Структура проекта
```
.
├── api
│   ├── __init__.py
│   ├── apps.py
│   ├── mixins.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── core
│   ├── utils
│   │   ├── __init__.py
│   │   └── foodsquery.py
│   ├── __init__.py
│   ├── apps.py
│   ├── fields.py
│   └── models.py
├── food
│   ├── migrations
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── food.py
│   │   └── foodcategory.py
│   ├── __init__.py
│   ├── admin.py
│   └── apps.py
├── foodies
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tests
│   ├── fixtures
│   │   ├── __init__.py
│   │   ├── fixture_data_foodcategory.py
│   │   └── fixture_data_foodrelations.py
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_food_and_rel.py
│   └── test_foodcategory.py
├── .env
├── django-entrypoint.sh
├── Dockerfile
├── README.md
├── manage.py
├── pytest.ini
├── requirements.txt
└── setup.cfg
```

----

## 📖 Installation
Docker и Pip.  
**Docker - образ уже содержит все миграции и созданного superuser.**  
**login: admin**  
**password: admin**

### Docker - образ с DockerHub

```
$ docker pull lilchiken/test-for-utf
$ docker run --name test-for-utf -p 8000:80 lilchiken/test-for-utf
# http://127.0.0.1:8000/
```

### Repo

```
$ git clone git@github.com:lilchiken/test-for-utf.git
$ cd test-for-utf
```

### Pip

```
# Windows
$ python -m venv .venv

# Linux / macOS
$ python3 -m venv venv

# Windows
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1

# Linux / macOS
$ source .venv/bin/activate

(.venv) $ pip install -r requirements.txt
(.venv) $ python3 manage.py migrate
(.venv) $ python3 manage.py createsuperuser
(.venv) $ python3 manage.py runserver 127.0.0.1:8000

# http://127.0.0.1:8000
```


### Docker - образ с репозитория

```
$ docker image build . -t test-for-utf
$ docker run -d --name test-for-utf -p 8000:80 test-for-utf
# http://127.0.0.1:8000
```

----

## Тесты / линтеры

### flake8
```
# в setup.cfg указанны настройки линтера
$ flake8 --append-config setup.cfg
$ flake8
```

### pytest
```
$ pytest
```
