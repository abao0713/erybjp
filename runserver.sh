#!/bin/bash
python manage.py db init
python manage.py db migrate --message "initial migration"
python manage.py db upgrade
python manage.py runserver -p 6851