#! /bin/bash

python /code/manage.py migrate --noinput;

#gunicorn -c gunicorn.conf.py elizarov.asgi:application --access-logfile -
python /code/manage.py runserver 0.0.0.0:8000