#!/bin/sh


# Collect static files
echo "Collect static files"
# python manage.py collectstatic --noinput --settings=challenge.local
python manage.py collectstatic --noinput --settings=${settings}
