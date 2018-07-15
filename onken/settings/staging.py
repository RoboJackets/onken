from onken.settings.development import *  # noqa: F401,F403

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

CAS_SERVER_URL = 'https://login.gatech.edu/cas/'

CAS_VERSION = 'CAS_2_SAML_1_0'

SILENCED_SYSTEM_CHECKS = 'security.W018,security.W004'
# security.W018: You should not have DEBUG set to True in deployment.
# This is a staging environment, so debug information is helpful, and not likely to affect "real" data.
#
# security.W004: You have not set a value for the SECURE_HSTS_SECONDS setting.
# HSTS is handled by Nginx.

DATADOG_TRACE = {
    'DEFAULT_SERVICE': 'onken',
    'TAGS': {'env': 'staging'},
    'ENABLED': True
}
