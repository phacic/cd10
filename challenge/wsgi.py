"""
WSGI config for challenge project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.cache import cache, caches

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challenge.settings')

application = get_wsgi_application()

# print(caches['default'].__dict__.get('_server'))
