#!/bin/sh

case $1 in
  setenv)
    export DJANGO_SUPERUSER_EMAIL=admin@admin.com
    export DJANGO_SUPERUSER_USERNAME=admin
    export DJANGO_SUPERUSER_PASSWORD=admin
    ;;
  migrate)
    python3 manage.py migrate
    python3 manage.py createsuperuser --username=admin --email=admin@admin.com --noinput
    ;;
  start)
    python3 manage.py runserver 0.0.0.0:80
    ;;
esac