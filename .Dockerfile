FROM python:3.8
EXPOSE 8000
WORKDIR /app 
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["flake8", "--append-config", "setup.cfg"]
CMD ["pytest"]
CMD ["manage.py", "runserver", "127.0.0.1:8000"]