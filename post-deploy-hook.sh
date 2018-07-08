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

# Run database migrations
./manage.py migrate

# Collect static files for nginx to serve
./manage.py collectstatic --noinput
