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

# ==============
# redis
# ==============
REDIS_HOST = os.environ.get('redis_host', '127.0.0.1')
REDIS_PORT = 6379
REDIS_CACHE_DB = 0
REDIS_PW = os.environ.get('redis_pwd', None)

# CACHE
CACHES = {
    "default": {
        # "BACKEND": "django_redis.cache.RedisCache",
        'BACKEND': 'redis_cache.RedisCache',
        "LOCATION": "redis://{host}:{port}/{db}".format(
            host=REDIS_HOST, port=REDIS_PORT, db=REDIS_CACHE_DB
        ),
        'KEY_PREFIX': 'ch-dev' if DEBUG else 'ch',
        "OPTIONS": {
            # "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PW,
            # use the latest version of pickle
            'PICKLE_VERSION': -1,
            # prevent exceptions when redis is down
            "IGNORE_EXCEPTIONS": True,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 100,
                'timeout': 20,
            },
        }
    }
}