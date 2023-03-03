FROM python:3.8.16-alpine3.17

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

# not supported by heroku
# EXPOSE 8000

# Run the image as a non-root user
RUN adduser -D myuser
USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT wsgi 

# #CMD [ "python", "manage.py", "runserver" ]

# ENTRYPOINT ["python3"]
# CMD ["manage.py", "runserver", "0.0.0.0:8000"]