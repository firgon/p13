FROM python:3.8.16-alpine3.17

ADD . /app/

WORKDIR /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python", "manage.py runserver" ]