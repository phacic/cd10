import os
from .settings import *

DEBUG = False
SECRET_KEY = os.environ.get('secret')

HOST = os.environ.get('allowed_host', '127.0.0.1')
ALLOWED_HOSTS = [
    'localhost', '127.0.0.1', HOST
]

# settings for drf
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],

    # default page size for pagination
    # 'PAGE_SIZE': 20
}

# ==============
# CORS
# ==============
CORS_ORIGIN_ALLOW_ALL = False
CORS_URLS_REGEX = '^.*$'  # all
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
]
CORS_ORIGIN_REGEX_WHITELIST = [
    # '^(https?://)?(\w+\.)?google\.com$',
    '^http://localhost',
    '^https://localhost',
    '^http://127.0.0.1',  # allow all from localhost
    '^https://127.0.0.1',  # allow all from localhost
]

# print email to console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
