FROM python:3.8.16-alpine3.17

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt --no-cache-dir

COPY . /app

# not supported by heroku
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
# run gunicorn
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT