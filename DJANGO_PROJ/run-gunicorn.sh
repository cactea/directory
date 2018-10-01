#!/bin/bash -e

# Waits for the database to be ready, migrates the database, uploads staticfiles, and runs the production server

python wait_for_postgres.py

python manage.py collectstatic --noinput

# Migrations must be made on the development host, committed, and run before starting the application.
#
# Be careful with concurrent access to the database. For production, the best strategy will be:
#   1. Stop all services using the database
#   2. Deploy & migrate
#   3. Restart services

python manage.py migrate

PYTHONPATH=. python ../scripts/populate.py

echo "Starting Gunicorn ..."

exec gunicorn shp.wsgi:application \
    --reload \
    --bind 0.0.0.0:8000 \
    --access-logfile - \
    --workers 3
