
# onken

[![GitHub license](https://img.shields.io/github/license/robojackets/onken.svg?style=flat-square)](https://raw.githubusercontent.com/robojackets/onken/master/LICENSE)
[![Maintainability](https://api.codeclimate.com/v1/badges/77e98a2e1f866f25c82d/maintainability)](https://codeclimate.com/github/RoboJackets/onken/maintainability)
[![Updates](https://pyup.io/repos/github/RoboJackets/onken/shield.svg)](https://pyup.io/repos/github/RoboJackets/onken/)
[![Known Vulnerabilities](https://snyk.io/test/github/RoboJackets/onken/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/RoboJackets/onken?targetFile=requirements.txt)
[![codecov](https://codecov.io/gh/RoboJackets/onken/branch/master/graph/badge.svg)](https://codecov.io/gh/RoboJackets/onken)
[![CircleCI](https://circleci.com/gh/RoboJackets/onken.svg?style=svg)](https://circleci.com/gh/RoboJackets/onken)

Onken is a tool for managing finances for student organizations.

## Developers' Guide

If you're interested in contributing to Onken, you'll need a few things installed on your machine.

### Python

This project is built using the Django framework for Python. You will need to have Python 3 installed to run it.

You will also need to create a Python virtual environment. There are many methods to do so, but the easiest is simply using the `virtualenv` package.

```shell
sudo pip3 install virtualenv
virtualenv ~/onken-env   # Change this parameter to wherever you'd like
```

### PostgreSQL

The package we use for supporting multiple workspaces from the same application instance depends on [PostgreSQL schemas](https://www.postgresql.org/docs/devel/static/ddl-schemas.html), so you will need to have PostgreSQL installed on your machine.

Note that the testing infrastructure will need access to create temporary databases when running your tests. The easiest way to do this is by giving the `postgres` user a password, and allowing `onken` to use that user.
#### Setting a password for the `postgres` user

```
$ sudo -u postgres psql
psql (10.4 (Ubuntu 10.4-0ubuntu0.18.04))
Type "help" for help.

postgres=# \password
Enter new password:
Enter it again:
postgres=# \quit
```

#### Creating a database

Even if you're using the `postgres` user, the database will need to already exist before you can start the application.

```
$ sudo -u postgres psql
psql (10.4 (Ubuntu 10.4-0ubuntu0.18.04))
Type "help" for help.

postgres=# CREATE DATABASE onken
CREATE DATABASE
postgres=# \quit
```

#### Configuring Onken to use your database

To avoid committing secrets in GitHub, this application will pull database information from the following environment variables:

 - `DJANGO_DATABASE_NAME`
 - `DJANGO_DATABASE_USER`
 - `DJANGO_DATABASE_PASSWORD`

You can set these in your virtual environment's activation script.

Additional configuration options are available - take a look at `onken.settings.development`.

### Mock Authentication Server

In production and staging environments, this application exclusively uses Georgia Tech Login (Apereo CAS) to authenticate users. To ensure a realistic testing environment, we've found a mock CAS server that mimicks that API and will allow you to provide arbitrary authentication information to the application. Note that you will need to have `node` and `npm` installed to run it.

```shell
# Install it globally to provide a command you can use anywhere
sudo npm install --global https://github.com/kberzinch/cas-server-mock

# Run it - the default development configuration expects http://localhost:3004/
csm --port 3004 --database ~/gt_example.json
```

The JSON file contains a list of all available users and the attributes that will be sent to the application. Here is an example.

```javascript
[
  {
    "name": "gburdell3",
    "attributes": {
      "givenName": "George",
      "sn": "Burdell",
      "email_primary": "george.burdell@gatech.edu"
    }
  }
]
```

### Mock Domain Names

Each workspace is available from a unique domain name. To test the application effectively, you'll need to set up several domains that point to `127.0.0.1`.

On Linux or Mac, this can be done by editing your `/etc/hosts` as root and adding entries in the below format.

```
127.0.0.1    onken.local
127.0.0.1    test1.onken.local
127.0.0.1    test2.onken.local
```

### Running the Application

Once you have all the above dependencies installed, you'll be able to run the application.

```shell
# Activate your virtual environment first and ensure csm is running in another terminal.

# First, run migrations to set up your database.
./manage.py migrate_schemas

# Create a public tenant once when setting up your environment - others can be added from the web management interface
./manage.py create_tenant --domain_url=onken.local --schema_name=public --name=public

# Create a user with super administrator permissions for accessing the web management interface
./manage.py create_tenant_superuser --username=gburdell3 --schema=public

# To run the built-in server for local testing
./manage.py runserver
```

Once the server is running, you can visit http://onken.local:8000/admin/ and create and manage workspaces and domains.
