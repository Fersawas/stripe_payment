#!/bin/bash

set -e

python manage.py wait_for_db
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py fill_db
python manage.py collectstatic --no-input

cp -r /app/staticfiles/. /static_dev/static/

gunicorn stripe_payment.wsgi:application --bind 0.0.0.0:8000 --reload