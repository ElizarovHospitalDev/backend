#! /bin/bash

python /code/manage.py migrate --noinput;

gunicorn -c gunicorn.conf.py elizarov.asgi:application --access-logfile -
