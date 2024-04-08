"""
WSGI config for drCandy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# change drCandy.settings.dev to .prod for production (or set param in config file)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drCandy.settings.dev')

application = get_wsgi_application()
