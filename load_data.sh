#!/bin/sh

# load initial data
echo "loading data"
python manage.py loaddata init-data.json --settings=${settings}