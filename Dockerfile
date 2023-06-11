FROM python:3.8
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
RUN chmod u+x /app/django-entrypoint.sh
RUN /bin/bash /app/django-entrypoint.sh migrate
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:80"]