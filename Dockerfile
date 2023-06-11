FROM python:3.8
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
CMD ["export", "DJANGO_SUPERUSER_EMAIL=admin@admin.com"]
CMD ["export", "DJANGO_SUPERUSER_USERNAME=admin"]
CMD ["export", "DJANGO_SUPERUSER_PASSWORD=admin"]
ENTRYPOINT ["python3"] 
CMD ["manage.py", "migrate"]
CMD ["manage.py", "createsuperuser", "--username=admin", "--email=admin@admin.com", "--noinput"]
CMD ["manage.py", "runserver", "0.0.0.0:80"]