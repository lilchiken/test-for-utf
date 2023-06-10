import pathlib

PROJECT_NAME = 'foodies'
BASE_DIR: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent

if not BASE_DIR.joinpath(PROJECT_NAME).is_dir:
    assert False, ('Проекта не найден!!!')

if not BASE_DIR.joinpath('manage.py').is_file():
    assert False, ('manage.py не найден!!!')

from django.utils.version import get_version
from rest_framework import VERSION

assert get_version() >= '3.2', (
    'Пожалуйста, используйте версию Django 3.2 или новее'
)
assert VERSION >= '3.12.0', (
    'Пожалуйста, используйте версию DRF 3.12.0 или новее'
)

from foodies.settings import (
    INSTALLED_APPS
)

app_gen = (
    app in INSTALLED_APPS for app in [
        'rest_framework',
        'api',
        'core',
        'food',
    ]
)

while True:
    try:
        assert next(app_gen), "Пожалуйста проверьте подключение приложений."
    except StopIteration:
        break

pytest_plugins = [
    'tests.fixtures.fixture_data_foodcategory',
    'tests.fixtures.fixture_data_foodrelations',
]