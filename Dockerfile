FROM python:3.8.16-alpine3.17

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

EXPOSE 8000

#CMD [ "python", "manage.py", "runserver" ]

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]