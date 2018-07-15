#!/bin/bash

# Abort deployment if any command fails
set -e
set -o pipefail

export DEPLOYMENT_START=$(date --iso-8601=seconds)

# Switch to the project directory
cd "${0%/*}"

# Enable the virtualenv
# shellcheck disable=SC1091
source venv/bin/activate

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
