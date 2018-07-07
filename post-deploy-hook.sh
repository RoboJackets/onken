#!/bin/bash

# Abort deployment if any command fails
set -e
set -o pipefail

# Switch to the project directory
cd "${0%/*}"

# Enable the virtualenv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt

# Run Django checks
./manage.py check --deploy

# Show database migrations
./manage.py showmigrations

# Run database migrations
./manage.py migrate

# Show database migrations again
./manage.py showmigrations

# Collect static files for nginx to serve
./manage.py collectstatic