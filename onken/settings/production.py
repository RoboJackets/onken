from onken.settings.staging import *  # noqa: F401,F403 lgtm[py/polluting-import]

DEBUG = False

SILENCED_SYSTEM_CHECKS = 'security.W004'
# security.W004: You have not set a value for the SECURE_HSTS_SECONDS setting.
# HSTS is handled by Nginx.


DATADOG_TRACE = {
    'DEFAULT_SERVICE': 'onken',
    'TAGS': {'env': 'production'}
}
