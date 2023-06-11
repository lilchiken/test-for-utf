#!/bin/sh

case $1 in
  migrate)
    export DJANGO_SUPERUSER_EMAIL=admin@admin.com
    export DJANGO_SUPERUSER_USERNAME=admin
    export DJANGO_SUPERUSER_PASSWORD=admin
    python3 manage.py migrate
    python3 manage.py createsuperuser --username=admin --email=admin@admin.com --noinput
    ;;
esac