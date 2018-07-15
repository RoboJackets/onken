from onken.settings.staging import *  # noqa: F401,F403 lgtm[py/polluting-import]

DEBUG = False

SILENCED_SYSTEM_CHECKS = 'security.W004'
# security.W004: You have not set a value for the SECURE_HSTS_SECONDS setting.
# HSTS is handled by Nginx.


DATADOG_TRACE = {
    'DEFAULT_SERVICE': 'onken',
    'TAGS': {'env': 'production'}
}


RAVEN_CONFIG = {
    'dsn': os.environ.get('DJANGO_RAVEN_DSN', None),
    'release': raven.fetch_git_sha(os.path.abspath(os.curdir)),
    'environment': 'production',
}
