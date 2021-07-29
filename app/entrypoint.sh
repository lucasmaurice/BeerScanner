#!/bin/sh
python3 manage.py makemigrations
python3 manage.py migrate --noinput
python3 manage.py runserver 0.0.0.0:8000

# nginx -g "daemon on;"

# uwsgi --socket localhost:8000 --chdir /app/ --wsgi-file webapp/wsgi.py --master --processes 2 --threads 1 --uid $APP_USER
