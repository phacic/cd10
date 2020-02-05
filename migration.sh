#!/bin/sh

# Apply database migrations
echo "Apply initial database migrations"
python manage.py makemigrations --settings=${settings}
python manage.py migrate --noinput --settings=${settings}