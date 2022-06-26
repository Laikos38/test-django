#!/bin/bash
echo "Migrate"
python manage.py migrate

echo "Load fixtures"
python manage.py loaddata fixture_1.json fixture_2.json

echo "Server"
python manage.py runserver 0.0.0.0:8000
