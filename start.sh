#!/bin/bash

python manage.py makemigrations&&
python manage.py migrate&&
gunicorn Resi_mysql.wsgi:application -c gunicorn.conf