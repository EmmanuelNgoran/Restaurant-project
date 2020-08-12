@echo off
python manage.py db stamp head
python manage.py db migrate -m %1
python manage.py db upgrade
