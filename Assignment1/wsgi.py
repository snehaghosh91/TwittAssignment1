"""
WSGI config for Assignment1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

os.environ("DJANGO_SETTINGS_MODULE", "Assignment1.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
