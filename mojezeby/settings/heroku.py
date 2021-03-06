import os

import dj_database_url

from .base import *

DEBUG = False

# transactional emails
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_API_KEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'MojeZeby.pl-Tools <noreply@mojezebypltoolsnotrealemail.com>'
ADMINS = [
    ('admin', os.getenv('ADMIN_EMAIL')),
]

ALLOWED_HOSTS = ['mojezebypl-tools.herokuapp.com']

# # Heroku: Update database configuration from $DATABASE_URL.
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# SECURITY
SECURE_HSTS_SECONDS = 31536000
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
