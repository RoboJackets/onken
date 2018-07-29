#!/bin/bash

export DEPLOYMENT_START=$(date --iso-8601=seconds)

# Switch to the project directory
cd "${0%/*}"

{ set +x; } 2>/dev/null
echo "+ source venv/bin/activate"
# Enable the virtualenv
# shellcheck disable=SC1091
source venv/bin/activate
set -x

# Install required packages
pip install -r requirements.txt

# Run Django checks
./manage.py check --deploy

# Run database migrations
./manage.py migrate_schemas

# Ask uWSGI to reload app
touch reload

# Collect static files for nginx to serve
./manage.py collectstatic --noinput

# Notify Sentry that the deployment completed
# shellcheck disable=SC1091
./notify-sentry.sh
